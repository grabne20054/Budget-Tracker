import { reactive } from "vue";
import { apiGetAccount, apiPostAccount } from "../api/accounts";
import { useLoadingStore } from "./loading";
import { useDialogStore } from "./dialog";
import { useAuthStore } from "../store/auth.js";

// data provider pattern : 
// https://www.patterns.dev/vue/data-provider

function useFetchAccounts() {
  const loadingStore = useLoadingStore();
  const dialogStore = useDialogStore();
  const authStore = useAuthStore();

  const accountList = reactive([
    {'balance': 0}
  ]);

  const fetchAccounts = async () => {
    loadingStore.setLoading();

    try {
      const res = await apiGetAccount();
      accountList.value = res.data;
      console.log(accountList.value)
    } catch (err) {
      console.log(err);
    } finally {
      // for loading test
      // setTimeout(() => {
      //   loadingStore.clearLoading();
      // }, 1000);
      loadingStore.clearLoading();
    }
  };

  fetchAccounts();

  return { accountList };
}

async function registerAccount(){
  const loadingStore = useLoadingStore();
  const dialogStore = useDialogStore();
  loadingStore.setLoading();

  apiPostAccount()
  .then((res) => {
    console.log(res);
    dialogStore.setSuccess({
      title: "Register Account Success",
      secondLine: "This dialog will close in 2 seconds",
    });
  })
  .catch((err) => {
    if (err.response.status != 400)
    {
      dialogStore.setError({
        title: "Register Account Failed",
        secondLine: "This dialog will close in 2 seconds",
      });
    }

  })
  .finally(() => {
    loadingStore.clearLoading();
    setTimeout(() => {
      dialogStore.reset();
    }, 2000);
  });
}


export { useFetchAccounts, registerAccount};
