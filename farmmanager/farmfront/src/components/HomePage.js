import "react-native-gesture-handler";
import React from "react";
import { View, StyleSheet, Text, TouchableOpacity, Button, Image } from "react-native";
import { NavigationContainer } from "@react-navigation/native";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { createStackNavigator } from "@react-navigation/stack";
import LandReportFinance from "./LandReportFinance";
import LandReportInventory from "./LandReportInventory";

const Stack = createStackNavigator();

export default function HomePage({ navigation }) {
  return (
    <View style={{ flex: 1 }}>
        <View style={{ flex: 1, flexDirection: "row" }}>
           <Image
              style={{
                alignSelf: "center",
                flex: 1, 
                flexDirection: "row",
                justifyContent: "center",
                paddingBottom: 10
              }}
              source={require("../images/homepage.jpg")}
            />
        </View>
      <View style={{ flex: 1 }}>
        <View style={{ flex: 1, flexDirection: "row" }}>
          <TouchableOpacity
            onPress={() => navigation.navigate("Finance")}
            style={{
              flex: 1,
              backgroundColor: "#7cb407",
              borderRadius: 20,
              margin: 10,
              fontSize: 24,
              justifyContent: "center",
              alignItems: "center"
            }}
          >
          <Image style={{
                alignSelf: "center",
                width: 80,
                height: 80,
                marginRight: 5
              }} source={require("../images/cashmoney.jpg")} />
            <Text>FINANCE</Text>
          </TouchableOpacity>
          <TouchableOpacity
            onPress={() => navigation.navigate("Stores")}
            style={{
              flex: 1,
              backgroundColor: "#7cb407",
              borderRadius: 20,
              margin: 10,
              fontSize: 24,
              justifyContent: "center",
              alignItems: "center"
            }}
          >
          <Image style={{
                alignSelf: "center",
                width: 80,
                height: 80,
                marginRight: 5
              }} source={require("../images/stores.png")} />
            <Text>STORES</Text>
          </TouchableOpacity>
        </View>
      </View>
      <View style={{ flex: 1 }}>
        <View
          style={{ flex: 1, flexDirection: "row" }}
        >
          <TouchableOpacity
            // onPress={() => navigation.navigate("")}
            style={{
              flex: 1,
              backgroundColor: "#606734",
              borderRadius: 5,
              margin: 10,
              fontSize: 24,
              justifyContent: "center",
              alignItems: "center"
            }}
          >
            <Text>UPDATES</Text>
          </TouchableOpacity>
        </View>
      </View>
    </View>
   );
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: 25
  },
  // nav: {
  //   flex: 0.7,
  //   flexDirection: "row",
  //   backgroundColor: "#ad2525",
  //   justifyContent: "center",
  //   alignItems: "center"
  // },
  // menu: {
  //   flex: 1,
  //   height: 90,
  //   alignItems: "flex-start",
  //   paddingLeft: 15,
  //   justifyContent: "center",
  //   color: "white"
  // },
  // detail: {
  //   flex: 1,
  //   justifyContent: "center",
  //   height: 90,
  //   alignItems: "flex-end",
  //   paddingRight: 15
  // },
  // finance: {
  //   backgroundColor: "green",
  //   flex: 2,
  //   justifyContent: "center",
  //   margin: 8,
  //   alignItems: "center"
  // },
  // inventory: {
  //   backgroundColor: "gray",
  //   margin: 8,
  //   flex: 2,
  //   alignItems: "center",
  //   justifyContent: "center"
  // },
  // update: {
  //   backgroundColor: "gray",
  //   margin: 8,
  //   flex: 1.3,
  //   justifyContent: "center",
  //   alignItems: "center"
  // },
  // text: {
  //   color: "white"
  // }
});
