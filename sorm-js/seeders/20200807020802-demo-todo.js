'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    /**
     * Add seed commands here.
     *
     * Example:
     * await queryInterface.bulkInsert('People', [{
     *   name: 'John Doe',
     *   isBetaMember: false
     * }], {});
    */
   const list_todos = [
    "Jalan2 jam 5:00 WIB",
    "Minum di Indomaret",
    "Swimming",
    "Kantor UT pondok cabe",
    "Makan Mie Ayam"
  ];

  let datas = [];

  for(let i = 0; i < 20000; i++){
    let rand_list = Math.round((Math.random() * (list_todos.length-1)) );
    let rand_done = Math.round(Math.random());

    let data = { todo_desc: list_todos[rand_list], is_completed: rand_done, createdAt: new Date() };
    datas.push(data);
  }

  await queryInterface.bulkInsert('Todos', datas, {});

  },

  down: async (queryInterface, Sequelize) => {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
  }
};
