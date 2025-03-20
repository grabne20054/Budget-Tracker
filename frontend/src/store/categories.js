import { reactive } from "vue";
import { apiGetCategories, apiPostCategory } from "../api/categories.js";
import { useLoadingStore } from "./loading";
import { useDialogStore } from "./dialog";
import { useAuthStore } from "../store/auth.js";

// data provider pattern : 
// https://www.patterns.dev/vue/data-provider

function useFetchCategories() {
  const loadingStore = useLoadingStore();
  const dialogStore = useDialogStore();
  const authStore = useAuthStore();

  const categoriesList = reactive([
    {'name': "", "description": ""}
  ]);

  const fetchCategories = async () => {
    loadingStore.setLoading();

    try {
      const res = await apiGetCategories();
      categoriesList.value = res.data;
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

  fetchCategories();

  return { categoriesList };
}

async function registerCategory(form){
  const loadingStore = useLoadingStore();
  const dialogStore = useDialogStore();
  loadingStore.setLoading();

  apiPostCategory(form)
  .then((res) => {
    console.log(res);
    dialogStore.setSuccess({
      title: "Register Category Success",
      secondLine: "This dialog will close in 2 seconds",
    });
  })
  .catch((err) => {
    
      dialogStore.setError({
        title: "Register Account Failed",
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


export { useFetchCategories, registerCategory};
