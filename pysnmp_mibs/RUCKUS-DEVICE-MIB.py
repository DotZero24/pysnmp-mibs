_J='static'
_I='ruckusDeviceWanIPIndex'
_H='RUCKUS-DEVICE-MIB'
_G='read-only'
_F='TruthValue'
_E='DisplayString'
_D='Integer32'
_C='OctetString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ruckusCommonDeviceModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusCommonDeviceModule')
RuckusCountryCode,=mibBuilder.importSymbols('RUCKUS-TC-MIB','RuckusCountryCode')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','TextualConvention',_F)
ruckusDeviceMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,1,4,1))
_RuckusDeviceObjects_ObjectIdentity=ObjectIdentity
ruckusDeviceObjects=_RuckusDeviceObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,1,4,1,1))
_RuckusDeviceInfo_ObjectIdentity=ObjectIdentity
ruckusDeviceInfo=_RuckusDeviceInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,4,1,1,1))
class _RuckusDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusDeviceName_Type.__name__=_E
_RuckusDeviceName_Object=MibScalar
ruckusDeviceName=_RuckusDeviceName_Object((1,3,6,1,4,1,25053,1,1,4,1,1,1,1),_RuckusDeviceName_Type())
ruckusDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceName.setStatus(_A)
class _RuckusDeviceReboot_Type(TruthValue):defaultValue=2
_RuckusDeviceReboot_Type.__name__=_F
_RuckusDeviceReboot_Object=MibScalar
ruckusDeviceReboot=_RuckusDeviceReboot_Object((1,3,6,1,4,1,25053,1,1,4,1,1,1,2),_RuckusDeviceReboot_Type())
ruckusDeviceReboot.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceReboot.setStatus(_A)
class _RuckusDeviceRebootWithDefaults_Type(TruthValue):defaultValue=2
_RuckusDeviceRebootWithDefaults_Type.__name__=_F
_RuckusDeviceRebootWithDefaults_Object=MibScalar
ruckusDeviceRebootWithDefaults=_RuckusDeviceRebootWithDefaults_Object((1,3,6,1,4,1,25053,1,1,4,1,1,1,3),_RuckusDeviceRebootWithDefaults_Type())
ruckusDeviceRebootWithDefaults.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceRebootWithDefaults.setStatus(_A)
_RuckusDeviceCountryCode_Type=RuckusCountryCode
_RuckusDeviceCountryCode_Object=MibScalar
ruckusDeviceCountryCode=_RuckusDeviceCountryCode_Object((1,3,6,1,4,1,25053,1,1,4,1,1,1,4),_RuckusDeviceCountryCode_Type())
ruckusDeviceCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceCountryCode.setStatus(_A)
class _RuckusDeviceGPS_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RuckusDeviceGPS_Type.__name__=_E
_RuckusDeviceGPS_Object=MibScalar
ruckusDeviceGPS=_RuckusDeviceGPS_Object((1,3,6,1,4,1,25053,1,1,4,1,1,1,5),_RuckusDeviceGPS_Type())
ruckusDeviceGPS.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceGPS.setStatus(_A)
class _RuckusDeviceNEId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusDeviceNEId_Type.__name__=_E
_RuckusDeviceNEId_Object=MibScalar
ruckusDeviceNEId=_RuckusDeviceNEId_Object((1,3,6,1,4,1,25053,1,1,4,1,1,1,6),_RuckusDeviceNEId_Type())
ruckusDeviceNEId.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceNEId.setStatus(_A)
class _RuckusDeviceLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RuckusDeviceLocation_Type.__name__=_E
_RuckusDeviceLocation_Object=MibScalar
ruckusDeviceLocation=_RuckusDeviceLocation_Object((1,3,6,1,4,1,25053,1,1,4,1,1,1,10),_RuckusDeviceLocation_Type())
ruckusDeviceLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceLocation.setStatus(_A)
_RuckusDeviceMacAddr_Type=MacAddress
_RuckusDeviceMacAddr_Object=MibScalar
ruckusDeviceMacAddr=_RuckusDeviceMacAddr_Object((1,3,6,1,4,1,25053,1,1,4,1,1,1,11),_RuckusDeviceMacAddr_Type())
ruckusDeviceMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusDeviceMacAddr.setStatus(_A)
_RuckusDeviceLedCtrl_Type=TruthValue
_RuckusDeviceLedCtrl_Object=MibScalar
ruckusDeviceLedCtrl=_RuckusDeviceLedCtrl_Object((1,3,6,1,4,1,25053,1,1,4,1,1,1,15),_RuckusDeviceLedCtrl_Type())
ruckusDeviceLedCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceLedCtrl.setStatus(_A)
_RuckusDeviceTrapInfo_ObjectIdentity=ObjectIdentity
ruckusDeviceTrapInfo=_RuckusDeviceTrapInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,4,1,1,2))
class _RuckusDeviceTrapDestination_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusDeviceTrapDestination_Type.__name__=_C
_RuckusDeviceTrapDestination_Object=MibScalar
ruckusDeviceTrapDestination=_RuckusDeviceTrapDestination_Object((1,3,6,1,4,1,25053,1,1,4,1,1,2,1),_RuckusDeviceTrapDestination_Type())
ruckusDeviceTrapDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceTrapDestination.setStatus(_A)
class _RuckusDeviceTrapDestination2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusDeviceTrapDestination2_Type.__name__=_C
_RuckusDeviceTrapDestination2_Object=MibScalar
ruckusDeviceTrapDestination2=_RuckusDeviceTrapDestination2_Object((1,3,6,1,4,1,25053,1,1,4,1,1,2,2),_RuckusDeviceTrapDestination2_Type())
ruckusDeviceTrapDestination2.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceTrapDestination2.setStatus(_A)
_RuckusDeviceIPInfo_ObjectIdentity=ObjectIdentity
ruckusDeviceIPInfo=_RuckusDeviceIPInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,4,1,1,3))
_RuckusDevicePrimaryDNS_Type=IpAddress
_RuckusDevicePrimaryDNS_Object=MibScalar
ruckusDevicePrimaryDNS=_RuckusDevicePrimaryDNS_Object((1,3,6,1,4,1,25053,1,1,4,1,1,3,1),_RuckusDevicePrimaryDNS_Type())
ruckusDevicePrimaryDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDevicePrimaryDNS.setStatus(_A)
_RuckusDeviceSecondaryDNS_Type=IpAddress
_RuckusDeviceSecondaryDNS_Object=MibScalar
ruckusDeviceSecondaryDNS=_RuckusDeviceSecondaryDNS_Object((1,3,6,1,4,1,25053,1,1,4,1,1,3,2),_RuckusDeviceSecondaryDNS_Type())
ruckusDeviceSecondaryDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceSecondaryDNS.setStatus(_A)
class _RuckusDevicePrimaryDNSIPV6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusDevicePrimaryDNSIPV6_Type.__name__=_C
_RuckusDevicePrimaryDNSIPV6_Object=MibScalar
ruckusDevicePrimaryDNSIPV6=_RuckusDevicePrimaryDNSIPV6_Object((1,3,6,1,4,1,25053,1,1,4,1,1,3,3),_RuckusDevicePrimaryDNSIPV6_Type())
ruckusDevicePrimaryDNSIPV6.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDevicePrimaryDNSIPV6.setStatus(_A)
class _RuckusDeviceSecondaryDNSIPV6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusDeviceSecondaryDNSIPV6_Type.__name__=_C
_RuckusDeviceSecondaryDNSIPV6_Object=MibScalar
ruckusDeviceSecondaryDNSIPV6=_RuckusDeviceSecondaryDNSIPV6_Object((1,3,6,1,4,1,25053,1,1,4,1,1,3,4),_RuckusDeviceSecondaryDNSIPV6_Type())
ruckusDeviceSecondaryDNSIPV6.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceSecondaryDNSIPV6.setStatus(_A)
_RuckusDeviceWanInfo_ObjectIdentity=ObjectIdentity
ruckusDeviceWanInfo=_RuckusDeviceWanInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,4,1,1,4))
_RuckusDeviceWanTable_Object=MibTable
ruckusDeviceWanTable=_RuckusDeviceWanTable_Object((1,3,6,1,4,1,25053,1,1,4,1,1,4,1))
if mibBuilder.loadTexts:ruckusDeviceWanTable.setStatus(_A)
_RuckusDeviceWanEntry_Object=MibTableRow
ruckusDeviceWanEntry=_RuckusDeviceWanEntry_Object((1,3,6,1,4,1,25053,1,1,4,1,1,4,1,1))
ruckusDeviceWanEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:ruckusDeviceWanEntry.setStatus(_A)
class _RuckusDeviceWanIPAddrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),(_J,2),('dhcp',3),('pppoe',4)))
_RuckusDeviceWanIPAddrMode_Type.__name__=_D
_RuckusDeviceWanIPAddrMode_Object=MibTableColumn
ruckusDeviceWanIPAddrMode=_RuckusDeviceWanIPAddrMode_Object((1,3,6,1,4,1,25053,1,1,4,1,1,4,1,1,1),_RuckusDeviceWanIPAddrMode_Type())
ruckusDeviceWanIPAddrMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceWanIPAddrMode.setStatus(_A)
_RuckusDeviceWanIPAddr_Type=IpAddress
_RuckusDeviceWanIPAddr_Object=MibTableColumn
ruckusDeviceWanIPAddr=_RuckusDeviceWanIPAddr_Object((1,3,6,1,4,1,25053,1,1,4,1,1,4,1,1,2),_RuckusDeviceWanIPAddr_Type())
ruckusDeviceWanIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceWanIPAddr.setStatus(_A)
_RuckusDeviceWanName_Type=DisplayString
_RuckusDeviceWanName_Object=MibTableColumn
ruckusDeviceWanName=_RuckusDeviceWanName_Object((1,3,6,1,4,1,25053,1,1,4,1,1,4,1,1,3),_RuckusDeviceWanName_Type())
ruckusDeviceWanName.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusDeviceWanName.setStatus(_A)
_RuckusDeviceWanNetmask_Type=IpAddress
_RuckusDeviceWanNetmask_Object=MibTableColumn
ruckusDeviceWanNetmask=_RuckusDeviceWanNetmask_Object((1,3,6,1,4,1,25053,1,1,4,1,1,4,1,1,4),_RuckusDeviceWanNetmask_Type())
ruckusDeviceWanNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceWanNetmask.setStatus(_A)
_RuckusDeviceWanGateway_Type=IpAddress
_RuckusDeviceWanGateway_Object=MibTableColumn
ruckusDeviceWanGateway=_RuckusDeviceWanGateway_Object((1,3,6,1,4,1,25053,1,1,4,1,1,4,1,1,5),_RuckusDeviceWanGateway_Type())
ruckusDeviceWanGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceWanGateway.setStatus(_A)
class _RuckusDeviceWanIPVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2),('dualstack',3)))
_RuckusDeviceWanIPVersion_Type.__name__=_D
_RuckusDeviceWanIPVersion_Object=MibTableColumn
ruckusDeviceWanIPVersion=_RuckusDeviceWanIPVersion_Object((1,3,6,1,4,1,25053,1,1,4,1,1,4,1,1,8),_RuckusDeviceWanIPVersion_Type())
ruckusDeviceWanIPVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceWanIPVersion.setStatus(_A)
class _RuckusDeviceWanIPV6AddrMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto-configuration',1),(_J,2)))
_RuckusDeviceWanIPV6AddrMode_Type.__name__=_D
_RuckusDeviceWanIPV6AddrMode_Object=MibTableColumn
ruckusDeviceWanIPV6AddrMode=_RuckusDeviceWanIPV6AddrMode_Object((1,3,6,1,4,1,25053,1,1,4,1,1,4,1,1,10),_RuckusDeviceWanIPV6AddrMode_Type())
ruckusDeviceWanIPV6AddrMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceWanIPV6AddrMode.setStatus(_A)
class _RuckusDeviceWanIPV6Addr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusDeviceWanIPV6Addr_Type.__name__=_C
_RuckusDeviceWanIPV6Addr_Object=MibTableColumn
ruckusDeviceWanIPV6Addr=_RuckusDeviceWanIPV6Addr_Object((1,3,6,1,4,1,25053,1,1,4,1,1,4,1,1,11),_RuckusDeviceWanIPV6Addr_Type())
ruckusDeviceWanIPV6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceWanIPV6Addr.setStatus(_A)
class _RuckusDeviceWanIPV6PrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,128))
_RuckusDeviceWanIPV6PrefixLen_Type.__name__=_D
_RuckusDeviceWanIPV6PrefixLen_Object=MibTableColumn
ruckusDeviceWanIPV6PrefixLen=_RuckusDeviceWanIPV6PrefixLen_Object((1,3,6,1,4,1,25053,1,1,4,1,1,4,1,1,12),_RuckusDeviceWanIPV6PrefixLen_Type())
ruckusDeviceWanIPV6PrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceWanIPV6PrefixLen.setStatus(_A)
class _RuckusDeviceWanIPV6Gateway_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusDeviceWanIPV6Gateway_Type.__name__=_C
_RuckusDeviceWanIPV6Gateway_Object=MibTableColumn
ruckusDeviceWanIPV6Gateway=_RuckusDeviceWanIPV6Gateway_Object((1,3,6,1,4,1,25053,1,1,4,1,1,4,1,1,13),_RuckusDeviceWanIPV6Gateway_Type())
ruckusDeviceWanIPV6Gateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusDeviceWanIPV6Gateway.setStatus(_A)
_RuckusDeviceWanIPIndex_Type=Unsigned32
_RuckusDeviceWanIPIndex_Object=MibTableColumn
ruckusDeviceWanIPIndex=_RuckusDeviceWanIPIndex_Object((1,3,6,1,4,1,25053,1,1,4,1,1,4,1,1,200),_RuckusDeviceWanIPIndex_Type())
ruckusDeviceWanIPIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ruckusDeviceWanIPIndex.setStatus(_A)
_RuckusDeviceEvents_ObjectIdentity=ObjectIdentity
ruckusDeviceEvents=_RuckusDeviceEvents_ObjectIdentity((1,3,6,1,4,1,25053,1,1,4,1,2))
mibBuilder.exportSymbols(_H,**{'ruckusDeviceMIB':ruckusDeviceMIB,'ruckusDeviceObjects':ruckusDeviceObjects,'ruckusDeviceInfo':ruckusDeviceInfo,'ruckusDeviceName':ruckusDeviceName,'ruckusDeviceReboot':ruckusDeviceReboot,'ruckusDeviceRebootWithDefaults':ruckusDeviceRebootWithDefaults,'ruckusDeviceCountryCode':ruckusDeviceCountryCode,'ruckusDeviceGPS':ruckusDeviceGPS,'ruckusDeviceNEId':ruckusDeviceNEId,'ruckusDeviceLocation':ruckusDeviceLocation,'ruckusDeviceMacAddr':ruckusDeviceMacAddr,'ruckusDeviceLedCtrl':ruckusDeviceLedCtrl,'ruckusDeviceTrapInfo':ruckusDeviceTrapInfo,'ruckusDeviceTrapDestination':ruckusDeviceTrapDestination,'ruckusDeviceTrapDestination2':ruckusDeviceTrapDestination2,'ruckusDeviceIPInfo':ruckusDeviceIPInfo,'ruckusDevicePrimaryDNS':ruckusDevicePrimaryDNS,'ruckusDeviceSecondaryDNS':ruckusDeviceSecondaryDNS,'ruckusDevicePrimaryDNSIPV6':ruckusDevicePrimaryDNSIPV6,'ruckusDeviceSecondaryDNSIPV6':ruckusDeviceSecondaryDNSIPV6,'ruckusDeviceWanInfo':ruckusDeviceWanInfo,'ruckusDeviceWanTable':ruckusDeviceWanTable,'ruckusDeviceWanEntry':ruckusDeviceWanEntry,'ruckusDeviceWanIPAddrMode':ruckusDeviceWanIPAddrMode,'ruckusDeviceWanIPAddr':ruckusDeviceWanIPAddr,'ruckusDeviceWanName':ruckusDeviceWanName,'ruckusDeviceWanNetmask':ruckusDeviceWanNetmask,'ruckusDeviceWanGateway':ruckusDeviceWanGateway,'ruckusDeviceWanIPVersion':ruckusDeviceWanIPVersion,'ruckusDeviceWanIPV6AddrMode':ruckusDeviceWanIPV6AddrMode,'ruckusDeviceWanIPV6Addr':ruckusDeviceWanIPV6Addr,'ruckusDeviceWanIPV6PrefixLen':ruckusDeviceWanIPV6PrefixLen,'ruckusDeviceWanIPV6Gateway':ruckusDeviceWanIPV6Gateway,_I:ruckusDeviceWanIPIndex,'ruckusDeviceEvents':ruckusDeviceEvents})