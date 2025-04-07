import { reactive } from "vue";
import { apiDeleteTransaction, apiGetLastNTransactions, apiGetTransactions, apiPostTransaction } from "../api/transactions.js";
import { useLoadingStore } from "./loading";
import { useDialogStore } from "./dialog";
import { useAuthStore } from "../store/auth.js";

// data provider pattern : 
// https://www.patterns.dev/vue/data-provider

function useFetchTransactions(limit = null) {
  const loadingStore = useLoadingStore();
  const dialogStore = useDialogStore();
  const authStore = useAuthStore();

  const transactionsList = reactive([
    {"paymentreason": "", "amount": 0, "type": "", "category_id": 0}
  ]);

  const fetchTransactions = async () => {
    loadingStore.setLoading();

    try {
      if (limit) {
        const res = await apiGetLastNTransactions(limit);
        transactionsList.value = res.data;
      } else {
        const res = await apiGetTransactions();
        transactionsList.value = res.data;
      }
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

  fetchTransactions();

  return { transactionsList };
}

async function registerTransaction(form){
  const loadingStore = useLoadingStore();
  const dialogStore = useDialogStore();
  loadingStore.setLoading();
  apiPostTransaction(form)
  .then((res) => {
    console.log(res);
    dialogStore.setSuccess({
      title: "Register Transaction Success",
      secondLine: "This dialog will close in 2 seconds",
    });
  })
  .catch((err) => {
    
      dialogStore.setError({
        title: "Register Transaction Failed",
        secondLine: "This dialog will close in 2 seconds",
      });

  })
  .finally(() => {
    loadingStore.clearLoading();
    setTimeout(() => {
      dialogStore.reset();
    }, 2000);
  });
}

async function deleteTransaction(transactionId){
  const loadingStore = useLoadingStore();
  const dialogStore = useDialogStore();
  loadingStore.setLoading();

  apiDeleteTransaction(transactionId)
  .then((res) => {
    console.log(res);
    dialogStore.setSuccess({
      title: "Delete Transaction Success",
      secondLine: "This dialog will close in 2 seconds",
    });
  })
  .catch((err) => {
    
      dialogStore.setError({
        title: "Delete Transaction Failed",
        secondLine: "This dialog will close in 2 seconds",
      });

  })
  .finally(() => {
    loadingStore.clearLoading();
    setTimeout(() => {
      dialogStore.reset();
    }, 2000);
  });
}


export { useFetchTransactions, registerTransaction, deleteTransaction };
