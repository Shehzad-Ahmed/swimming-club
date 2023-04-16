const storeReducer = (state, action) => {
  switch (action.type) {
    case 'USER_SIGN_IN':
      localStorage.setItem('userDetails', JSON.stringify(action.payload));
      return {
        ...state,
        userDetails: { ...action.payload },
      };
    case 'USER_SIGN_OUT':
      localStorage.setItem('userDetails', null);
      return {
        ...state,
        userDetails: null,
      };
    default:
      return state;
  }
};

export default storeReducer;
