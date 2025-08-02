_J='ruckusSZConfigWLANID'
_I='RUCKUS-SZ-CONFIG-WLAN-MIB'
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
ruckusSZWLANModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusSZWLANModule')
RuckusAdminStatus,RuckusRadioMode,RuckusRateLimiting,RuckusSSID,RuckusdB=mibBuilder.importSymbols('RUCKUS-TC-MIB','RuckusAdminStatus','RuckusRadioMode','RuckusRateLimiting','RuckusSSID','RuckusdB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
ruckusSZConfigWLANMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,4,2,2))
if mibBuilder.loadTexts:ruckusSZConfigWLANMIB.setRevisions(('2020-06-15 11:00',))
_RuckusSZConfigWLANObjects_ObjectIdentity=ObjectIdentity
ruckusSZConfigWLANObjects=_RuckusSZConfigWLANObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,4,2,2,1))
_RuckusSZConfigWLAN_ObjectIdentity=ObjectIdentity
ruckusSZConfigWLAN=_RuckusSZConfigWLAN_ObjectIdentity((1,3,6,1,4,1,25053,1,4,2,2,1,1))
_RuckusSZConfigWLANTable_Object=MibTable
ruckusSZConfigWLANTable=_RuckusSZConfigWLANTable_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1))
if mibBuilder.loadTexts:ruckusSZConfigWLANTable.setStatus(_A)
_RuckusSZConfigWLANEntry_Object=MibTableRow
ruckusSZConfigWLANEntry=_RuckusSZConfigWLANEntry_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1))
ruckusSZConfigWLANEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:ruckusSZConfigWLANEntry.setStatus(_A)
class _RuckusSZConfigWLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RuckusSZConfigWLANID_Type.__name__=_B
_RuckusSZConfigWLANID_Object=MibTableColumn
ruckusSZConfigWLANID=_RuckusSZConfigWLANID_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,1),_RuckusSZConfigWLANID_Type())
ruckusSZConfigWLANID.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSZConfigWLANID.setStatus(_A)
class _RuckusSZConfigWLANSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,32))
_RuckusSZConfigWLANSSID_Type.__name__=_D
_RuckusSZConfigWLANSSID_Object=MibTableColumn
ruckusSZConfigWLANSSID=_RuckusSZConfigWLANSSID_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,2),_RuckusSZConfigWLANSSID_Type())
ruckusSZConfigWLANSSID.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSZConfigWLANSSID.setStatus(_A)
class _RuckusSZConfigWLANDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RuckusSZConfigWLANDescription_Type.__name__=_H
_RuckusSZConfigWLANDescription_Object=MibTableColumn
ruckusSZConfigWLANDescription=_RuckusSZConfigWLANDescription_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,3),_RuckusSZConfigWLANDescription_Type())
ruckusSZConfigWLANDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSZConfigWLANDescription.setStatus(_A)
class _RuckusSZConfigWLANName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,32))
_RuckusSZConfigWLANName_Type.__name__=_D
_RuckusSZConfigWLANName_Object=MibTableColumn
ruckusSZConfigWLANName=_RuckusSZConfigWLANName_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,4),_RuckusSZConfigWLANName_Type())
ruckusSZConfigWLANName.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSZConfigWLANName.setStatus(_A)
class _RuckusSZConfigWLANWLANServiceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('standardUsage',1),('hotspot',2),('guest',3),('webauth',4),('hotspot20',5),('hotspot20-osen',6),('weChat',7)))
_RuckusSZConfigWLANWLANServiceType_Type.__name__=_B
_RuckusSZConfigWLANWLANServiceType_Object=MibTableColumn
ruckusSZConfigWLANWLANServiceType=_RuckusSZConfigWLANWLANServiceType_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,8),_RuckusSZConfigWLANWLANServiceType_Type())
ruckusSZConfigWLANWLANServiceType.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSZConfigWLANWLANServiceType.setStatus(_A)
class _RuckusSZConfigWLANAuthentication_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('open',1),('eap',2),('mac-address',3),('eapMacAddress',4)))
_RuckusSZConfigWLANAuthentication_Type.__name__=_B
_RuckusSZConfigWLANAuthentication_Object=MibTableColumn
ruckusSZConfigWLANAuthentication=_RuckusSZConfigWLANAuthentication_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,10),_RuckusSZConfigWLANAuthentication_Type())
ruckusSZConfigWLANAuthentication.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSZConfigWLANAuthentication.setStatus(_A)
class _RuckusSZConfigWLANEncryption_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('wpa2',1),('wpa-Mixed',2),('wep-64',3),('wep-128',4),('none-enc',5),('wpa3',6),('wpa2Wpa3Mixed',7),('owe',8)))
_RuckusSZConfigWLANEncryption_Type.__name__=_B
_RuckusSZConfigWLANEncryption_Object=MibTableColumn
ruckusSZConfigWLANEncryption=_RuckusSZConfigWLANEncryption_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,12),_RuckusSZConfigWLANEncryption_Type())
ruckusSZConfigWLANEncryption.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSZConfigWLANEncryption.setStatus(_A)
class _RuckusSZConfigWLANWEPKeyIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_RuckusSZConfigWLANWEPKeyIndex_Type.__name__=_B
_RuckusSZConfigWLANWEPKeyIndex_Object=MibTableColumn
ruckusSZConfigWLANWEPKeyIndex=_RuckusSZConfigWLANWEPKeyIndex_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,15),_RuckusSZConfigWLANWEPKeyIndex_Type())
ruckusSZConfigWLANWEPKeyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSZConfigWLANWEPKeyIndex.setStatus(_A)
class _RuckusSZConfigWLANWEPKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10),ValueSizeConstraint(26,26))
_RuckusSZConfigWLANWEPKey_Type.__name__=_D
_RuckusSZConfigWLANWEPKey_Object=MibTableColumn
ruckusSZConfigWLANWEPKey=_RuckusSZConfigWLANWEPKey_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,16),_RuckusSZConfigWLANWEPKey_Type())
ruckusSZConfigWLANWEPKey.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSZConfigWLANWEPKey.setStatus(_A)
class _RuckusSZConfigWLANWPACipherType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('aes',1),('tkipaes',2),('null',3),('aesGCMP256',4)))
_RuckusSZConfigWLANWPACipherType_Type.__name__=_B
_RuckusSZConfigWLANWPACipherType_Object=MibTableColumn
ruckusSZConfigWLANWPACipherType=_RuckusSZConfigWLANWPACipherType_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,20),_RuckusSZConfigWLANWPACipherType_Type())
ruckusSZConfigWLANWPACipherType.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSZConfigWLANWPACipherType.setStatus(_A)
class _RuckusSZConfigWLANWPAKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,63),ValueSizeConstraint(64,64))
_RuckusSZConfigWLANWPAKey_Type.__name__=_D
_RuckusSZConfigWLANWPAKey_Object=MibTableColumn
ruckusSZConfigWLANWPAKey=_RuckusSZConfigWLANWPAKey_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,21),_RuckusSZConfigWLANWPAKey_Type())
ruckusSZConfigWLANWPAKey.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSZConfigWLANWPAKey.setStatus(_A)
class _RuckusSZConfigWLANSAEPassphrase_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,63),ValueSizeConstraint(64,64))
_RuckusSZConfigWLANSAEPassphrase_Type.__name__=_D
_RuckusSZConfigWLANSAEPassphrase_Object=MibTableColumn
ruckusSZConfigWLANSAEPassphrase=_RuckusSZConfigWLANSAEPassphrase_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,23),_RuckusSZConfigWLANSAEPassphrase_Type())
ruckusSZConfigWLANSAEPassphrase.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSZConfigWLANSAEPassphrase.setStatus(_A)
class _RuckusSZConfigWLANWirelessClientIsolation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RuckusSZConfigWLANWirelessClientIsolation_Type.__name__=_B
_RuckusSZConfigWLANWirelessClientIsolation_Object=MibTableColumn
ruckusSZConfigWLANWirelessClientIsolation=_RuckusSZConfigWLANWirelessClientIsolation_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,28),_RuckusSZConfigWLANWirelessClientIsolation_Type())
ruckusSZConfigWLANWirelessClientIsolation.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSZConfigWLANWirelessClientIsolation.setStatus(_A)
class _RuckusSZConfigWLANZeroITActivation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RuckusSZConfigWLANZeroITActivation_Type.__name__=_B
_RuckusSZConfigWLANZeroITActivation_Object=MibTableColumn
ruckusSZConfigWLANZeroITActivation=_RuckusSZConfigWLANZeroITActivation_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,30),_RuckusSZConfigWLANZeroITActivation_Type())
ruckusSZConfigWLANZeroITActivation.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSZConfigWLANZeroITActivation.setStatus(_A)
class _RuckusSZConfigWLANServicePriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('high',1),('low',2)))
_RuckusSZConfigWLANServicePriority_Type.__name__=_B
_RuckusSZConfigWLANServicePriority_Object=MibTableColumn
ruckusSZConfigWLANServicePriority=_RuckusSZConfigWLANServicePriority_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,32),_RuckusSZConfigWLANServicePriority_Type())
ruckusSZConfigWLANServicePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSZConfigWLANServicePriority.setStatus(_A)
class _RuckusSZConfigWLANAccountingUpdateInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_RuckusSZConfigWLANAccountingUpdateInterval_Type.__name__=_B
_RuckusSZConfigWLANAccountingUpdateInterval_Object=MibTableColumn
ruckusSZConfigWLANAccountingUpdateInterval=_RuckusSZConfigWLANAccountingUpdateInterval_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,36),_RuckusSZConfigWLANAccountingUpdateInterval_Type())
ruckusSZConfigWLANAccountingUpdateInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSZConfigWLANAccountingUpdateInterval.setStatus(_A)
class _RuckusSZConfigWLANVlanID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RuckusSZConfigWLANVlanID_Type.__name__=_B
_RuckusSZConfigWLANVlanID_Object=MibTableColumn
ruckusSZConfigWLANVlanID=_RuckusSZConfigWLANVlanID_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,45),_RuckusSZConfigWLANVlanID_Type())
ruckusSZConfigWLANVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSZConfigWLANVlanID.setStatus(_A)
class _RuckusSZConfigWLANHideSSID_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_RuckusSZConfigWLANHideSSID_Type.__name__=_B
_RuckusSZConfigWLANHideSSID_Object=MibTableColumn
ruckusSZConfigWLANHideSSID=_RuckusSZConfigWLANHideSSID_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,50),_RuckusSZConfigWLANHideSSID_Type())
ruckusSZConfigWLANHideSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSZConfigWLANHideSSID.setStatus(_A)
class _RuckusSZConfigWLANMaxClientsPerAP_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_RuckusSZConfigWLANMaxClientsPerAP_Type.__name__=_B
_RuckusSZConfigWLANMaxClientsPerAP_Object=MibTableColumn
ruckusSZConfigWLANMaxClientsPerAP=_RuckusSZConfigWLANMaxClientsPerAP_Object((1,3,6,1,4,1,25053,1,4,2,2,1,1,1,1,55),_RuckusSZConfigWLANMaxClientsPerAP_Type())
ruckusSZConfigWLANMaxClientsPerAP.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusSZConfigWLANMaxClientsPerAP.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'ruckusSZConfigWLANMIB':ruckusSZConfigWLANMIB,'ruckusSZConfigWLANObjects':ruckusSZConfigWLANObjects,'ruckusSZConfigWLAN':ruckusSZConfigWLAN,'ruckusSZConfigWLANTable':ruckusSZConfigWLANTable,'ruckusSZConfigWLANEntry':ruckusSZConfigWLANEntry,_J:ruckusSZConfigWLANID,'ruckusSZConfigWLANSSID':ruckusSZConfigWLANSSID,'ruckusSZConfigWLANDescription':ruckusSZConfigWLANDescription,'ruckusSZConfigWLANName':ruckusSZConfigWLANName,'ruckusSZConfigWLANWLANServiceType':ruckusSZConfigWLANWLANServiceType,'ruckusSZConfigWLANAuthentication':ruckusSZConfigWLANAuthentication,'ruckusSZConfigWLANEncryption':ruckusSZConfigWLANEncryption,'ruckusSZConfigWLANWEPKeyIndex':ruckusSZConfigWLANWEPKeyIndex,'ruckusSZConfigWLANWEPKey':ruckusSZConfigWLANWEPKey,'ruckusSZConfigWLANWPACipherType':ruckusSZConfigWLANWPACipherType,'ruckusSZConfigWLANWPAKey':ruckusSZConfigWLANWPAKey,'ruckusSZConfigWLANSAEPassphrase':ruckusSZConfigWLANSAEPassphrase,'ruckusSZConfigWLANWirelessClientIsolation':ruckusSZConfigWLANWirelessClientIsolation,'ruckusSZConfigWLANZeroITActivation':ruckusSZConfigWLANZeroITActivation,'ruckusSZConfigWLANServicePriority':ruckusSZConfigWLANServicePriority,'ruckusSZConfigWLANAccountingUpdateInterval':ruckusSZConfigWLANAccountingUpdateInterval,'ruckusSZConfigWLANVlanID':ruckusSZConfigWLANVlanID,'ruckusSZConfigWLANHideSSID':ruckusSZConfigWLANHideSSID,'ruckusSZConfigWLANMaxClientsPerAP':ruckusSZConfigWLANMaxClientsPerAP})