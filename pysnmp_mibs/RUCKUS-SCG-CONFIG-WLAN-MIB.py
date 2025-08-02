_J='ruckusSCGConfigWLANID'
_I='RUCKUS-SCG-CONFIG-WLAN-MIB'
_H='DisplayString'
_G='disable'
_F='enable'
_E='read-only'
_D='OctetString'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ruckusSCGWLANModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusSCGWLANModule')
RuckusAdminStatus,RuckusRadioMode,RuckusRateLimiting,RuckusSSID,RuckusdB=mibBuilder.importSymbols('RUCKUS-TC-MIB','RuckusAdminStatus','RuckusRadioMode','RuckusRateLimiting','RuckusSSID','RuckusdB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
ruckusSCGConfigWLANMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,3,2,2))
_RuckusSCGConfigWLANObjects_ObjectIdentity=ObjectIdentity
ruckusSCGConfigWLANObjects=_RuckusSCGConfigWLANObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,3,2,2,1))
_RuckusSCGConfigWLAN_ObjectIdentity=ObjectIdentity
ruckusSCGConfigWLAN=_RuckusSCGConfigWLAN_ObjectIdentity((1,3,6,1,4,1,25053,1,3,2,2,1,1))
_RuckusSCGConfigWLANTable_Object=MibTable
ruckusSCGConfigWLANTable=_RuckusSCGConfigWLANTable_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1))
if mibBuilder.loadTexts:ruckusSCGConfigWLANTable.setStatus(_A)
_RuckusSCGConfigWLANEntry_Object=MibTableRow
ruckusSCGConfigWLANEntry=_RuckusSCGConfigWLANEntry_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1))
ruckusSCGConfigWLANEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:ruckusSCGConfigWLANEntry.setStatus(_A)
class _RuckusSCGConfigWLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RuckusSCGConfigWLANID_Type.__name__=_B
_RuckusSCGConfigWLANID_Object=MibTableColumn
ruckusSCGConfigWLANID=_RuckusSCGConfigWLANID_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,1),_RuckusSCGConfigWLANID_Type())
ruckusSCGConfigWLANID.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSCGConfigWLANID.setStatus(_A)
class _RuckusSCGConfigWLANSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,32))
_RuckusSCGConfigWLANSSID_Type.__name__=_D
_RuckusSCGConfigWLANSSID_Object=MibTableColumn
ruckusSCGConfigWLANSSID=_RuckusSCGConfigWLANSSID_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,2),_RuckusSCGConfigWLANSSID_Type())
ruckusSCGConfigWLANSSID.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSCGConfigWLANSSID.setStatus(_A)
class _RuckusSCGConfigWLANDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RuckusSCGConfigWLANDescription_Type.__name__=_H
_RuckusSCGConfigWLANDescription_Object=MibTableColumn
ruckusSCGConfigWLANDescription=_RuckusSCGConfigWLANDescription_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,3),_RuckusSCGConfigWLANDescription_Type())
ruckusSCGConfigWLANDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSCGConfigWLANDescription.setStatus(_A)
class _RuckusSCGConfigWLANName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,32))
_RuckusSCGConfigWLANName_Type.__name__=_D
_RuckusSCGConfigWLANName_Object=MibTableColumn
ruckusSCGConfigWLANName=_RuckusSCGConfigWLANName_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,4),_RuckusSCGConfigWLANName_Type())
ruckusSCGConfigWLANName.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSCGConfigWLANName.setStatus(_A)
class _RuckusSCGZoneName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RuckusSCGZoneName_Type.__name__=_D
_RuckusSCGZoneName_Object=MibTableColumn
ruckusSCGZoneName=_RuckusSCGZoneName_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,5),_RuckusSCGZoneName_Type())
ruckusSCGZoneName.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSCGZoneName.setStatus(_A)
class _RuckusSCGConfigWLANWLANServiceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('standardUsage',1),('hotspot',2),('guest',3),('webauth',4),('hotspot20',5),('hotspot20-osen',6)))
_RuckusSCGConfigWLANWLANServiceType_Type.__name__=_B
_RuckusSCGConfigWLANWLANServiceType_Object=MibTableColumn
ruckusSCGConfigWLANWLANServiceType=_RuckusSCGConfigWLANWLANServiceType_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,8),_RuckusSCGConfigWLANWLANServiceType_Type())
ruckusSCGConfigWLANWLANServiceType.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSCGConfigWLANWLANServiceType.setStatus(_A)
class _RuckusSCGConfigWLANAuthentication_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('open',1),('eap',2),('mac-address',3)))
_RuckusSCGConfigWLANAuthentication_Type.__name__=_B
_RuckusSCGConfigWLANAuthentication_Object=MibTableColumn
ruckusSCGConfigWLANAuthentication=_RuckusSCGConfigWLANAuthentication_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,10),_RuckusSCGConfigWLANAuthentication_Type())
ruckusSCGConfigWLANAuthentication.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSCGConfigWLANAuthentication.setStatus(_A)
class _RuckusSCGConfigWLANEncryption_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('wpa2',1),('wpa-Mixed',2),('wep-64',3),('wep-128',4),('none-enc',5)))
_RuckusSCGConfigWLANEncryption_Type.__name__=_B
_RuckusSCGConfigWLANEncryption_Object=MibTableColumn
ruckusSCGConfigWLANEncryption=_RuckusSCGConfigWLANEncryption_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,12),_RuckusSCGConfigWLANEncryption_Type())
ruckusSCGConfigWLANEncryption.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSCGConfigWLANEncryption.setStatus(_A)
class _RuckusSCGConfigWLANWEPKeyIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_RuckusSCGConfigWLANWEPKeyIndex_Type.__name__=_B
_RuckusSCGConfigWLANWEPKeyIndex_Object=MibTableColumn
ruckusSCGConfigWLANWEPKeyIndex=_RuckusSCGConfigWLANWEPKeyIndex_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,15),_RuckusSCGConfigWLANWEPKeyIndex_Type())
ruckusSCGConfigWLANWEPKeyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSCGConfigWLANWEPKeyIndex.setStatus(_A)
class _RuckusSCGConfigWLANWEPKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10),ValueSizeConstraint(26,26))
_RuckusSCGConfigWLANWEPKey_Type.__name__=_D
_RuckusSCGConfigWLANWEPKey_Object=MibTableColumn
ruckusSCGConfigWLANWEPKey=_RuckusSCGConfigWLANWEPKey_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,16),_RuckusSCGConfigWLANWEPKey_Type())
ruckusSCGConfigWLANWEPKey.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSCGConfigWLANWEPKey.setStatus(_A)
class _RuckusSCGConfigWLANWPACipherType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('aes',1),('tkipaes',2),('null',3)))
_RuckusSCGConfigWLANWPACipherType_Type.__name__=_B
_RuckusSCGConfigWLANWPACipherType_Object=MibTableColumn
ruckusSCGConfigWLANWPACipherType=_RuckusSCGConfigWLANWPACipherType_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,20),_RuckusSCGConfigWLANWPACipherType_Type())
ruckusSCGConfigWLANWPACipherType.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSCGConfigWLANWPACipherType.setStatus(_A)
class _RuckusSCGConfigWLANWPAKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,63),ValueSizeConstraint(64,64))
_RuckusSCGConfigWLANWPAKey_Type.__name__=_D
_RuckusSCGConfigWLANWPAKey_Object=MibTableColumn
ruckusSCGConfigWLANWPAKey=_RuckusSCGConfigWLANWPAKey_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,21),_RuckusSCGConfigWLANWPAKey_Type())
ruckusSCGConfigWLANWPAKey.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSCGConfigWLANWPAKey.setStatus(_A)
class _RuckusSCGConfigWLANWirelessClientIsolation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RuckusSCGConfigWLANWirelessClientIsolation_Type.__name__=_B
_RuckusSCGConfigWLANWirelessClientIsolation_Object=MibTableColumn
ruckusSCGConfigWLANWirelessClientIsolation=_RuckusSCGConfigWLANWirelessClientIsolation_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,28),_RuckusSCGConfigWLANWirelessClientIsolation_Type())
ruckusSCGConfigWLANWirelessClientIsolation.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSCGConfigWLANWirelessClientIsolation.setStatus(_A)
class _RuckusSCGConfigWLANZeroITActivation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RuckusSCGConfigWLANZeroITActivation_Type.__name__=_B
_RuckusSCGConfigWLANZeroITActivation_Object=MibTableColumn
ruckusSCGConfigWLANZeroITActivation=_RuckusSCGConfigWLANZeroITActivation_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,30),_RuckusSCGConfigWLANZeroITActivation_Type())
ruckusSCGConfigWLANZeroITActivation.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSCGConfigWLANZeroITActivation.setStatus(_A)
class _RuckusSCGConfigWLANServicePriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('high',1),('low',2)))
_RuckusSCGConfigWLANServicePriority_Type.__name__=_B
_RuckusSCGConfigWLANServicePriority_Object=MibTableColumn
ruckusSCGConfigWLANServicePriority=_RuckusSCGConfigWLANServicePriority_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,32),_RuckusSCGConfigWLANServicePriority_Type())
ruckusSCGConfigWLANServicePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSCGConfigWLANServicePriority.setStatus(_A)
class _RuckusSCGConfigWLANAccountingUpdateInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_RuckusSCGConfigWLANAccountingUpdateInterval_Type.__name__=_B
_RuckusSCGConfigWLANAccountingUpdateInterval_Object=MibTableColumn
ruckusSCGConfigWLANAccountingUpdateInterval=_RuckusSCGConfigWLANAccountingUpdateInterval_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,36),_RuckusSCGConfigWLANAccountingUpdateInterval_Type())
ruckusSCGConfigWLANAccountingUpdateInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSCGConfigWLANAccountingUpdateInterval.setStatus(_A)
class _RuckusSCGConfigWLANVlanID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RuckusSCGConfigWLANVlanID_Type.__name__=_B
_RuckusSCGConfigWLANVlanID_Object=MibTableColumn
ruckusSCGConfigWLANVlanID=_RuckusSCGConfigWLANVlanID_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,45),_RuckusSCGConfigWLANVlanID_Type())
ruckusSCGConfigWLANVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSCGConfigWLANVlanID.setStatus(_A)
class _RuckusSCGConfigWLANHideSSID_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RuckusSCGConfigWLANHideSSID_Type.__name__=_B
_RuckusSCGConfigWLANHideSSID_Object=MibTableColumn
ruckusSCGConfigWLANHideSSID=_RuckusSCGConfigWLANHideSSID_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,50),_RuckusSCGConfigWLANHideSSID_Type())
ruckusSCGConfigWLANHideSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSCGConfigWLANHideSSID.setStatus(_A)
class _RuckusSCGConfigWLANMaxClientsPerAP_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_RuckusSCGConfigWLANMaxClientsPerAP_Type.__name__=_B
_RuckusSCGConfigWLANMaxClientsPerAP_Object=MibTableColumn
ruckusSCGConfigWLANMaxClientsPerAP=_RuckusSCGConfigWLANMaxClientsPerAP_Object((1,3,6,1,4,1,25053,1,3,2,2,1,1,1,1,55),_RuckusSCGConfigWLANMaxClientsPerAP_Type())
ruckusSCGConfigWLANMaxClientsPerAP.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSCGConfigWLANMaxClientsPerAP.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'ruckusSCGConfigWLANMIB':ruckusSCGConfigWLANMIB,'ruckusSCGConfigWLANObjects':ruckusSCGConfigWLANObjects,'ruckusSCGConfigWLAN':ruckusSCGConfigWLAN,'ruckusSCGConfigWLANTable':ruckusSCGConfigWLANTable,'ruckusSCGConfigWLANEntry':ruckusSCGConfigWLANEntry,_J:ruckusSCGConfigWLANID,'ruckusSCGConfigWLANSSID':ruckusSCGConfigWLANSSID,'ruckusSCGConfigWLANDescription':ruckusSCGConfigWLANDescription,'ruckusSCGConfigWLANName':ruckusSCGConfigWLANName,'ruckusSCGZoneName':ruckusSCGZoneName,'ruckusSCGConfigWLANWLANServiceType':ruckusSCGConfigWLANWLANServiceType,'ruckusSCGConfigWLANAuthentication':ruckusSCGConfigWLANAuthentication,'ruckusSCGConfigWLANEncryption':ruckusSCGConfigWLANEncryption,'ruckusSCGConfigWLANWEPKeyIndex':ruckusSCGConfigWLANWEPKeyIndex,'ruckusSCGConfigWLANWEPKey':ruckusSCGConfigWLANWEPKey,'ruckusSCGConfigWLANWPACipherType':ruckusSCGConfigWLANWPACipherType,'ruckusSCGConfigWLANWPAKey':ruckusSCGConfigWLANWPAKey,'ruckusSCGConfigWLANWirelessClientIsolation':ruckusSCGConfigWLANWirelessClientIsolation,'ruckusSCGConfigWLANZeroITActivation':ruckusSCGConfigWLANZeroITActivation,'ruckusSCGConfigWLANServicePriority':ruckusSCGConfigWLANServicePriority,'ruckusSCGConfigWLANAccountingUpdateInterval':ruckusSCGConfigWLANAccountingUpdateInterval,'ruckusSCGConfigWLANVlanID':ruckusSCGConfigWLANVlanID,'ruckusSCGConfigWLANHideSSID':ruckusSCGConfigWLANHideSSID,'ruckusSCGConfigWLANMaxClientsPerAP':ruckusSCGConfigWLANMaxClientsPerAP})