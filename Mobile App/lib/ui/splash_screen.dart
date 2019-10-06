import 'dart:async';

import 'package:flutter/material.dart';
//import 'package:whatsapp/pages/camera_screen.dart';

class SplashScreen extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => new SplashScreenState();
}

class SplashScreenState extends State<SplashScreen> {

  startTime() {
    var _duration = new Duration(seconds: 5);
    return new Timer(_duration , navigationPage );
  }

  navigationPage() {
    Navigator.of(context).pushNamed('/');
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    startTime();
  }

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return new Scaffold(
      backgroundColor: Colors.redAccent,
      body: new Stack(
        fit: StackFit.expand,
        children: <Widget>[
          new Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              new Container(
                width: 125,
                height : 125,
                decoration: new BoxDecoration(
                  image: new DecorationImage(
                      image: new AssetImage("assets/login_logo.png")
                  )
                ),

              ),
              new Text("مربی تست" , style: TextStyle(fontSize: 20 , color : Colors.white , fontWeight: FontWeight.bold,fontFamily:'Lalezar'))
            ],
          ),
          new Padding(
            padding: const EdgeInsets.only(bottom: 30),
            child: new Align(
              alignment: Alignment.bottomCenter,
              child: new CircularProgressIndicator(backgroundColor: Colors.white,),
            ),
          )
        ],
      )
    );
  }
}