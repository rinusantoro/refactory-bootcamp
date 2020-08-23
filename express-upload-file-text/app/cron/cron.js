module.exports = async nodemailer => {

    let configMail, transporter, emailTarget, mail;

  
    configMail = {
      service: 'gmail',
      auth: {
        user: 'bluut022@gmail.com',
        pass: 'UptT1kUT'
      }
    };
  
    transporter = await nodemailer.createTransport(configMail);
    emailTarget = 'rinusantoro@gmail.com';
  
    mail = {
      to: emailTarget,
      from: configMail.auth.user,
      subject: 'Total Belanja Pagi Ini',
      html: `<p>Total belanja Anda hari ini adalah Rp. 250.000, terima kasih</p>`
    };
    transporter.sendMail(mail);

    
}