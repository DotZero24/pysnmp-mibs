_AJ='etsysAntiSpoofNotificationGroup'
_AI='etsysAntiSpoofIpBindingGroup'
_AH='etsysAntiSpoofPortBindingGroup'
_AG='etsysAntiSpoofMacBindingGroup'
_AF='etsysAntiSpoofStationBindingGroup'
_AE='etsysAntiSpoofPortGroup'
_AD='etsysAntiSpoofThresholdGroup'
_AC='etsysAntiSpoofClassGroup'
_AB='etsysAntiSpoofSystemGroup'
_AA='etsysAntiSpoofDuplicateIpNotification'
_A9='etsysAntiSpoofClassNotification'
_A8='etsysAntiSpoofPortBindingClearBinding'
_A7='etsysAntiSpoofPortStationBindingIndex'
_A6='etsysAntiSpoofIpBindingClearBinding'
_A5='etsysAntiSpoofIpStationBindingIndex'
_A4='etsysAntiSpoofMacBindingClearBinding'
_A3='etsysAntiSpoofMacStationBindingIndex'
_A2='etsysAntiSpoofStationBindingEntryExpirationTime'
_A1='etsysAntiSpoofStationBindingEntryDurationTime'
_A0='etsysAntiSpoofStationBindingEntryBindingType'
_z='etsysAntiSpoofStationBindingEntryClearBinding'
_y='etsysAntiSpoofStationBindingEntryClearPortCounter'
_x='etsysAntiSpoofStationBindingEntryPortCounter'
_w='etsysAntiSpoofStationBindingEntryClearInetCounter'
_v='etsysAntiSpoofStationBindingEntryInetCounter'
_u='etsysAntiSpoofPortType'
_t='etsysAntiSpoofUntrustedTrafficPacketCounter'
_s='etsysAntiSpoofPortClassIndex'
_r='etsysAntiSpoofIpInspection'
_q='etsysAntiSpoofArpInspection'
_p='etsysAntiSpoofDHCPMacVerify'
_o='etsysAntiSpoofDHCPMode'
_n='etsysAntiSpoofThresholdType'
_m='etsysAntiSpoofThresholdActionQuarantineValue'
_l='etsysAntiSpoofThresholdActionMask'
_k='etsysAntiSpoofClassTimeout'
_j='etsysAntiSpoofClassName'
_i='etsysAntiSpoofSupportedBindingTypes'
_h='etsysAntiSpoofSupportedThresholdTypes'
_g='etsysAntiSpoofSupportedActionTypes'
_f='etsysAntiSpoofDuplicateIpControl'
_e='etsysAntiSpoofSystemNotificationInterval'
_d='etsysAntiSpoofSystemSnmpNotifications'
_c='etsysAntiSpoofMaxClassThresholdIndex'
_b='etsysAntiSpoofMaxClassIndex'
_a='etsysAntiSpoofSystemState'
_Z='etsysAntiSpoofStationBindingEntryIndex'
_Y='AntiSpoofPortType'
_X='etsysAntiSpoofThresholdIndex'
_W='portChange'
_V='ipv6Change'
_U='ipv4Change'
_T='SnmpAdminString'
_S='etsysAntiSpoofThresholdValue'
_R='AntiSpoofInspectionType'
_Q='etsysAntiSpoofClassIndex'
_P='Bits'
_O='ifIndex'
_N='IF-MIB'
_M='etsysAntiSpoofStationBindingEntryIfIndex'
_L='etsysAntiSpoofStationBindingInterface'
_K='not-accessible'
_J='seconds'
_I='Unsigned32'
_H='EnabledStatus'
_G='etsysAntiSpoofStationBindingEntryInetAddr'
_F='etsysAntiSpoofStationBindingEntryInetAddrType'
_E='etsysAntiSpoofStationBindingEntryMacAddr'
_D='read-only'
_C='read-write'
_B='ENTERASYS-ANTI-SPOOF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_N,'InterfaceIndex','InterfaceIndexOrZero',_O)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_T)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_P,'Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
etsysAntiSpoofMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,96))
if mibBuilder.loadTexts:etsysAntiSpoofMIB.setRevisions(('2013-01-15 16:31','2012-10-31 13:55'))
class AntiSpoofPortAction(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('generateSyslog',0),('generateNotification',1),('quarantineUser',2)))
class AntiSpoofInspectionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),('inspectionOnly',3)))
class AntiSpoofThresholdType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_V,2),(_W,3)))
class AntiSpoofPortType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('trusted',1),('bypass',2),('untrusted',3)))
class AntiSpoofBindingType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dhcp',1),('arp',2),('ip',3)))
class EtsysInstanceOID(TextualConvention,ObjectIdentifier):status=_A
_EtsysAntiSpoofObjects_ObjectIdentity=ObjectIdentity
etsysAntiSpoofObjects=_EtsysAntiSpoofObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,96,1))
_EtsysAntiSpoofNotificationBranch_ObjectIdentity=ObjectIdentity
etsysAntiSpoofNotificationBranch=_EtsysAntiSpoofNotificationBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,96,1,0))
_EtsysAntiSpoofSystemBranch_ObjectIdentity=ObjectIdentity
etsysAntiSpoofSystemBranch=_EtsysAntiSpoofSystemBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,96,1,1))
class _EtsysAntiSpoofSystemState_Type(EnabledStatus):defaultValue=2
_EtsysAntiSpoofSystemState_Type.__name__=_H
_EtsysAntiSpoofSystemState_Object=MibScalar
etsysAntiSpoofSystemState=_EtsysAntiSpoofSystemState_Object((1,3,6,1,4,1,5624,1,2,96,1,1,1),_EtsysAntiSpoofSystemState_Type())
etsysAntiSpoofSystemState.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofSystemState.setStatus(_A)
_EtsysAntiSpoofMaxClassIndex_Type=Unsigned32
_EtsysAntiSpoofMaxClassIndex_Object=MibScalar
etsysAntiSpoofMaxClassIndex=_EtsysAntiSpoofMaxClassIndex_Object((1,3,6,1,4,1,5624,1,2,96,1,1,2),_EtsysAntiSpoofMaxClassIndex_Type())
etsysAntiSpoofMaxClassIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofMaxClassIndex.setStatus(_A)
_EtsysAntiSpoofMaxClassThresholdIndex_Type=Unsigned32
_EtsysAntiSpoofMaxClassThresholdIndex_Object=MibScalar
etsysAntiSpoofMaxClassThresholdIndex=_EtsysAntiSpoofMaxClassThresholdIndex_Object((1,3,6,1,4,1,5624,1,2,96,1,1,3),_EtsysAntiSpoofMaxClassThresholdIndex_Type())
etsysAntiSpoofMaxClassThresholdIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofMaxClassThresholdIndex.setStatus(_A)
class _EtsysAntiSpoofSystemSnmpNotifications_Type(EnabledStatus):defaultValue=1
_EtsysAntiSpoofSystemSnmpNotifications_Type.__name__=_H
_EtsysAntiSpoofSystemSnmpNotifications_Object=MibScalar
etsysAntiSpoofSystemSnmpNotifications=_EtsysAntiSpoofSystemSnmpNotifications_Object((1,3,6,1,4,1,5624,1,2,96,1,1,4),_EtsysAntiSpoofSystemSnmpNotifications_Type())
etsysAntiSpoofSystemSnmpNotifications.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofSystemSnmpNotifications.setStatus(_A)
class _EtsysAntiSpoofSystemNotificationInterval_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_EtsysAntiSpoofSystemNotificationInterval_Type.__name__=_I
_EtsysAntiSpoofSystemNotificationInterval_Object=MibScalar
etsysAntiSpoofSystemNotificationInterval=_EtsysAntiSpoofSystemNotificationInterval_Object((1,3,6,1,4,1,5624,1,2,96,1,1,5),_EtsysAntiSpoofSystemNotificationInterval_Type())
etsysAntiSpoofSystemNotificationInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofSystemNotificationInterval.setStatus(_A)
if mibBuilder.loadTexts:etsysAntiSpoofSystemNotificationInterval.setUnits(_J)
class _EtsysAntiSpoofDuplicateIpControl_Type(EnabledStatus):defaultValue=2
_EtsysAntiSpoofDuplicateIpControl_Type.__name__=_H
_EtsysAntiSpoofDuplicateIpControl_Object=MibScalar
etsysAntiSpoofDuplicateIpControl=_EtsysAntiSpoofDuplicateIpControl_Object((1,3,6,1,4,1,5624,1,2,96,1,1,6),_EtsysAntiSpoofDuplicateIpControl_Type())
etsysAntiSpoofDuplicateIpControl.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofDuplicateIpControl.setStatus(_A)
_EtsysAntiSpoofSupportedActionTypes_Type=AntiSpoofPortAction
_EtsysAntiSpoofSupportedActionTypes_Object=MibScalar
etsysAntiSpoofSupportedActionTypes=_EtsysAntiSpoofSupportedActionTypes_Object((1,3,6,1,4,1,5624,1,2,96,1,1,7),_EtsysAntiSpoofSupportedActionTypes_Type())
etsysAntiSpoofSupportedActionTypes.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofSupportedActionTypes.setStatus(_A)
class _EtsysAntiSpoofSupportedThresholdTypes_Type(Bits):namedValues=NamedValues(*((_U,0),(_V,1),(_W,2)))
_EtsysAntiSpoofSupportedThresholdTypes_Type.__name__=_P
_EtsysAntiSpoofSupportedThresholdTypes_Object=MibScalar
etsysAntiSpoofSupportedThresholdTypes=_EtsysAntiSpoofSupportedThresholdTypes_Object((1,3,6,1,4,1,5624,1,2,96,1,1,8),_EtsysAntiSpoofSupportedThresholdTypes_Type())
etsysAntiSpoofSupportedThresholdTypes.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofSupportedThresholdTypes.setStatus(_A)
class _EtsysAntiSpoofSupportedBindingTypes_Type(Bits):namedValues=NamedValues(*(('dhcp',0),('arp',1),('ip',2)))
_EtsysAntiSpoofSupportedBindingTypes_Type.__name__=_P
_EtsysAntiSpoofSupportedBindingTypes_Object=MibScalar
etsysAntiSpoofSupportedBindingTypes=_EtsysAntiSpoofSupportedBindingTypes_Object((1,3,6,1,4,1,5624,1,2,96,1,1,9),_EtsysAntiSpoofSupportedBindingTypes_Type())
etsysAntiSpoofSupportedBindingTypes.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofSupportedBindingTypes.setStatus(_A)
_EtsysAntiSpoofClassBranch_ObjectIdentity=ObjectIdentity
etsysAntiSpoofClassBranch=_EtsysAntiSpoofClassBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,96,1,2))
_EtsysAntiSpoofClassTable_Object=MibTable
etsysAntiSpoofClassTable=_EtsysAntiSpoofClassTable_Object((1,3,6,1,4,1,5624,1,2,96,1,2,1))
if mibBuilder.loadTexts:etsysAntiSpoofClassTable.setStatus(_A)
_EtsysAntiSpoofClassEntry_Object=MibTableRow
etsysAntiSpoofClassEntry=_EtsysAntiSpoofClassEntry_Object((1,3,6,1,4,1,5624,1,2,96,1,2,1,1))
etsysAntiSpoofClassEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:etsysAntiSpoofClassEntry.setStatus(_A)
_EtsysAntiSpoofClassIndex_Type=Unsigned32
_EtsysAntiSpoofClassIndex_Object=MibTableColumn
etsysAntiSpoofClassIndex=_EtsysAntiSpoofClassIndex_Object((1,3,6,1,4,1,5624,1,2,96,1,2,1,1,1),_EtsysAntiSpoofClassIndex_Type())
etsysAntiSpoofClassIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:etsysAntiSpoofClassIndex.setStatus(_A)
class _EtsysAntiSpoofClassName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EtsysAntiSpoofClassName_Type.__name__=_T
_EtsysAntiSpoofClassName_Object=MibTableColumn
etsysAntiSpoofClassName=_EtsysAntiSpoofClassName_Object((1,3,6,1,4,1,5624,1,2,96,1,2,1,1,2),_EtsysAntiSpoofClassName_Type())
etsysAntiSpoofClassName.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofClassName.setStatus(_A)
class _EtsysAntiSpoofClassTimeout_Type(Unsigned32):defaultValue=600
_EtsysAntiSpoofClassTimeout_Type.__name__=_I
_EtsysAntiSpoofClassTimeout_Object=MibTableColumn
etsysAntiSpoofClassTimeout=_EtsysAntiSpoofClassTimeout_Object((1,3,6,1,4,1,5624,1,2,96,1,2,1,1,3),_EtsysAntiSpoofClassTimeout_Type())
etsysAntiSpoofClassTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofClassTimeout.setStatus(_A)
if mibBuilder.loadTexts:etsysAntiSpoofClassTimeout.setUnits(_J)
_EtsysAntiSpoofThresholdTable_Object=MibTable
etsysAntiSpoofThresholdTable=_EtsysAntiSpoofThresholdTable_Object((1,3,6,1,4,1,5624,1,2,96,1,2,2))
if mibBuilder.loadTexts:etsysAntiSpoofThresholdTable.setStatus(_A)
_EtsysAntiSpoofThresholdEntry_Object=MibTableRow
etsysAntiSpoofThresholdEntry=_EtsysAntiSpoofThresholdEntry_Object((1,3,6,1,4,1,5624,1,2,96,1,2,2,1))
etsysAntiSpoofThresholdEntry.setIndexNames((0,_B,_Q),(0,_B,_X))
if mibBuilder.loadTexts:etsysAntiSpoofThresholdEntry.setStatus(_A)
_EtsysAntiSpoofThresholdIndex_Type=Unsigned32
_EtsysAntiSpoofThresholdIndex_Object=MibTableColumn
etsysAntiSpoofThresholdIndex=_EtsysAntiSpoofThresholdIndex_Object((1,3,6,1,4,1,5624,1,2,96,1,2,2,1,1),_EtsysAntiSpoofThresholdIndex_Type())
etsysAntiSpoofThresholdIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:etsysAntiSpoofThresholdIndex.setStatus(_A)
_EtsysAntiSpoofThresholdValue_Type=Unsigned32
_EtsysAntiSpoofThresholdValue_Object=MibTableColumn
etsysAntiSpoofThresholdValue=_EtsysAntiSpoofThresholdValue_Object((1,3,6,1,4,1,5624,1,2,96,1,2,2,1,2),_EtsysAntiSpoofThresholdValue_Type())
etsysAntiSpoofThresholdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofThresholdValue.setStatus(_A)
_EtsysAntiSpoofThresholdActionMask_Type=AntiSpoofPortAction
_EtsysAntiSpoofThresholdActionMask_Object=MibTableColumn
etsysAntiSpoofThresholdActionMask=_EtsysAntiSpoofThresholdActionMask_Object((1,3,6,1,4,1,5624,1,2,96,1,2,2,1,3),_EtsysAntiSpoofThresholdActionMask_Type())
etsysAntiSpoofThresholdActionMask.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofThresholdActionMask.setStatus(_A)
_EtsysAntiSpoofThresholdActionQuarantineValue_Type=Integer32
_EtsysAntiSpoofThresholdActionQuarantineValue_Object=MibTableColumn
etsysAntiSpoofThresholdActionQuarantineValue=_EtsysAntiSpoofThresholdActionQuarantineValue_Object((1,3,6,1,4,1,5624,1,2,96,1,2,2,1,4),_EtsysAntiSpoofThresholdActionQuarantineValue_Type())
etsysAntiSpoofThresholdActionQuarantineValue.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofThresholdActionQuarantineValue.setStatus(_A)
_EtsysAntiSpoofThresholdType_Type=AntiSpoofThresholdType
_EtsysAntiSpoofThresholdType_Object=MibTableColumn
etsysAntiSpoofThresholdType=_EtsysAntiSpoofThresholdType_Object((1,3,6,1,4,1,5624,1,2,96,1,2,2,1,5),_EtsysAntiSpoofThresholdType_Type())
etsysAntiSpoofThresholdType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofThresholdType.setStatus(_A)
_EtsysAntiSpoofPortBranch_ObjectIdentity=ObjectIdentity
etsysAntiSpoofPortBranch=_EtsysAntiSpoofPortBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,96,1,3))
_EtsysAntiSpoofPortConfigTable_Object=MibTable
etsysAntiSpoofPortConfigTable=_EtsysAntiSpoofPortConfigTable_Object((1,3,6,1,4,1,5624,1,2,96,1,3,1))
if mibBuilder.loadTexts:etsysAntiSpoofPortConfigTable.setStatus(_A)
_EtsysAntiSpoofPortConfigEntry_Object=MibTableRow
etsysAntiSpoofPortConfigEntry=_EtsysAntiSpoofPortConfigEntry_Object((1,3,6,1,4,1,5624,1,2,96,1,3,1,1))
etsysAntiSpoofPortConfigEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:etsysAntiSpoofPortConfigEntry.setStatus(_A)
class _EtsysAntiSpoofDHCPMode_Type(EnabledStatus):defaultValue=2
_EtsysAntiSpoofDHCPMode_Type.__name__=_H
_EtsysAntiSpoofDHCPMode_Object=MibTableColumn
etsysAntiSpoofDHCPMode=_EtsysAntiSpoofDHCPMode_Object((1,3,6,1,4,1,5624,1,2,96,1,3,1,1,1),_EtsysAntiSpoofDHCPMode_Type())
etsysAntiSpoofDHCPMode.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofDHCPMode.setStatus(_A)
class _EtsysAntiSpoofDHCPMacVerify_Type(EnabledStatus):defaultValue=2
_EtsysAntiSpoofDHCPMacVerify_Type.__name__=_H
_EtsysAntiSpoofDHCPMacVerify_Object=MibTableColumn
etsysAntiSpoofDHCPMacVerify=_EtsysAntiSpoofDHCPMacVerify_Object((1,3,6,1,4,1,5624,1,2,96,1,3,1,1,2),_EtsysAntiSpoofDHCPMacVerify_Type())
etsysAntiSpoofDHCPMacVerify.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofDHCPMacVerify.setStatus(_A)
class _EtsysAntiSpoofArpInspection_Type(AntiSpoofInspectionType):defaultValue=2
_EtsysAntiSpoofArpInspection_Type.__name__=_R
_EtsysAntiSpoofArpInspection_Object=MibTableColumn
etsysAntiSpoofArpInspection=_EtsysAntiSpoofArpInspection_Object((1,3,6,1,4,1,5624,1,2,96,1,3,1,1,3),_EtsysAntiSpoofArpInspection_Type())
etsysAntiSpoofArpInspection.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofArpInspection.setStatus(_A)
class _EtsysAntiSpoofIpInspection_Type(AntiSpoofInspectionType):defaultValue=2
_EtsysAntiSpoofIpInspection_Type.__name__=_R
_EtsysAntiSpoofIpInspection_Object=MibTableColumn
etsysAntiSpoofIpInspection=_EtsysAntiSpoofIpInspection_Object((1,3,6,1,4,1,5624,1,2,96,1,3,1,1,4),_EtsysAntiSpoofIpInspection_Type())
etsysAntiSpoofIpInspection.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofIpInspection.setStatus(_A)
class _EtsysAntiSpoofPortClassIndex_Type(Unsigned32):defaultValue=0
_EtsysAntiSpoofPortClassIndex_Type.__name__=_I
_EtsysAntiSpoofPortClassIndex_Object=MibTableColumn
etsysAntiSpoofPortClassIndex=_EtsysAntiSpoofPortClassIndex_Object((1,3,6,1,4,1,5624,1,2,96,1,3,1,1,5),_EtsysAntiSpoofPortClassIndex_Type())
etsysAntiSpoofPortClassIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofPortClassIndex.setStatus(_A)
_EtsysAntiSpoofUntrustedTrafficPacketCounter_Type=Counter32
_EtsysAntiSpoofUntrustedTrafficPacketCounter_Object=MibTableColumn
etsysAntiSpoofUntrustedTrafficPacketCounter=_EtsysAntiSpoofUntrustedTrafficPacketCounter_Object((1,3,6,1,4,1,5624,1,2,96,1,3,1,1,6),_EtsysAntiSpoofUntrustedTrafficPacketCounter_Type())
etsysAntiSpoofUntrustedTrafficPacketCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofUntrustedTrafficPacketCounter.setStatus(_A)
_EtsysAntiSpoofPortTypeTable_Object=MibTable
etsysAntiSpoofPortTypeTable=_EtsysAntiSpoofPortTypeTable_Object((1,3,6,1,4,1,5624,1,2,96,1,3,2))
if mibBuilder.loadTexts:etsysAntiSpoofPortTypeTable.setStatus(_A)
_EtsysAntiSpoofPortTypeEntry_Object=MibTableRow
etsysAntiSpoofPortTypeEntry=_EtsysAntiSpoofPortTypeEntry_Object((1,3,6,1,4,1,5624,1,2,96,1,3,2,1))
etsysAntiSpoofPortTypeEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:etsysAntiSpoofPortTypeEntry.setStatus(_A)
class _EtsysAntiSpoofPortType_Type(AntiSpoofPortType):defaultValue=3
_EtsysAntiSpoofPortType_Type.__name__=_Y
_EtsysAntiSpoofPortType_Object=MibTableColumn
etsysAntiSpoofPortType=_EtsysAntiSpoofPortType_Object((1,3,6,1,4,1,5624,1,2,96,1,3,2,1,1),_EtsysAntiSpoofPortType_Type())
etsysAntiSpoofPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofPortType.setStatus(_A)
_EtsysAntiSpoofBindingBranch_ObjectIdentity=ObjectIdentity
etsysAntiSpoofBindingBranch=_EtsysAntiSpoofBindingBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,96,1,4))
_EtsysAntiSpoofStationBindingTable_Object=MibTable
etsysAntiSpoofStationBindingTable=_EtsysAntiSpoofStationBindingTable_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1))
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingTable.setStatus(_A)
_EtsysAntiSpoofStationBindingEntry_Object=MibTableRow
etsysAntiSpoofStationBindingEntry=_EtsysAntiSpoofStationBindingEntry_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1,1))
etsysAntiSpoofStationBindingEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntry.setStatus(_A)
_EtsysAntiSpoofStationBindingEntryIndex_Type=EtsysInstanceOID
_EtsysAntiSpoofStationBindingEntryIndex_Object=MibTableColumn
etsysAntiSpoofStationBindingEntryIndex=_EtsysAntiSpoofStationBindingEntryIndex_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1,1,1),_EtsysAntiSpoofStationBindingEntryIndex_Type())
etsysAntiSpoofStationBindingEntryIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryIndex.setStatus(_A)
_EtsysAntiSpoofStationBindingEntryMacAddr_Type=MacAddress
_EtsysAntiSpoofStationBindingEntryMacAddr_Object=MibTableColumn
etsysAntiSpoofStationBindingEntryMacAddr=_EtsysAntiSpoofStationBindingEntryMacAddr_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1,1,2),_EtsysAntiSpoofStationBindingEntryMacAddr_Type())
etsysAntiSpoofStationBindingEntryMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryMacAddr.setStatus(_A)
_EtsysAntiSpoofStationBindingEntryInetAddrType_Type=InetAddressType
_EtsysAntiSpoofStationBindingEntryInetAddrType_Object=MibTableColumn
etsysAntiSpoofStationBindingEntryInetAddrType=_EtsysAntiSpoofStationBindingEntryInetAddrType_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1,1,3),_EtsysAntiSpoofStationBindingEntryInetAddrType_Type())
etsysAntiSpoofStationBindingEntryInetAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryInetAddrType.setStatus(_A)
_EtsysAntiSpoofStationBindingEntryInetAddr_Type=InetAddress
_EtsysAntiSpoofStationBindingEntryInetAddr_Object=MibTableColumn
etsysAntiSpoofStationBindingEntryInetAddr=_EtsysAntiSpoofStationBindingEntryInetAddr_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1,1,4),_EtsysAntiSpoofStationBindingEntryInetAddr_Type())
etsysAntiSpoofStationBindingEntryInetAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryInetAddr.setStatus(_A)
_EtsysAntiSpoofStationBindingEntryIfIndex_Type=InterfaceIndex
_EtsysAntiSpoofStationBindingEntryIfIndex_Object=MibTableColumn
etsysAntiSpoofStationBindingEntryIfIndex=_EtsysAntiSpoofStationBindingEntryIfIndex_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1,1,5),_EtsysAntiSpoofStationBindingEntryIfIndex_Type())
etsysAntiSpoofStationBindingEntryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryIfIndex.setStatus(_A)
_EtsysAntiSpoofStationBindingEntryInetCounter_Type=Counter32
_EtsysAntiSpoofStationBindingEntryInetCounter_Object=MibTableColumn
etsysAntiSpoofStationBindingEntryInetCounter=_EtsysAntiSpoofStationBindingEntryInetCounter_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1,1,6),_EtsysAntiSpoofStationBindingEntryInetCounter_Type())
etsysAntiSpoofStationBindingEntryInetCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryInetCounter.setStatus(_A)
_EtsysAntiSpoofStationBindingEntryClearInetCounter_Type=TruthValue
_EtsysAntiSpoofStationBindingEntryClearInetCounter_Object=MibTableColumn
etsysAntiSpoofStationBindingEntryClearInetCounter=_EtsysAntiSpoofStationBindingEntryClearInetCounter_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1,1,7),_EtsysAntiSpoofStationBindingEntryClearInetCounter_Type())
etsysAntiSpoofStationBindingEntryClearInetCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryClearInetCounter.setStatus(_A)
_EtsysAntiSpoofStationBindingEntryPortCounter_Type=Counter32
_EtsysAntiSpoofStationBindingEntryPortCounter_Object=MibTableColumn
etsysAntiSpoofStationBindingEntryPortCounter=_EtsysAntiSpoofStationBindingEntryPortCounter_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1,1,8),_EtsysAntiSpoofStationBindingEntryPortCounter_Type())
etsysAntiSpoofStationBindingEntryPortCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryPortCounter.setStatus(_A)
_EtsysAntiSpoofStationBindingEntryClearPortCounter_Type=TruthValue
_EtsysAntiSpoofStationBindingEntryClearPortCounter_Object=MibTableColumn
etsysAntiSpoofStationBindingEntryClearPortCounter=_EtsysAntiSpoofStationBindingEntryClearPortCounter_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1,1,9),_EtsysAntiSpoofStationBindingEntryClearPortCounter_Type())
etsysAntiSpoofStationBindingEntryClearPortCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryClearPortCounter.setStatus(_A)
_EtsysAntiSpoofStationBindingEntryClearBinding_Type=TruthValue
_EtsysAntiSpoofStationBindingEntryClearBinding_Object=MibTableColumn
etsysAntiSpoofStationBindingEntryClearBinding=_EtsysAntiSpoofStationBindingEntryClearBinding_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1,1,10),_EtsysAntiSpoofStationBindingEntryClearBinding_Type())
etsysAntiSpoofStationBindingEntryClearBinding.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryClearBinding.setStatus(_A)
_EtsysAntiSpoofStationBindingEntryBindingType_Type=AntiSpoofBindingType
_EtsysAntiSpoofStationBindingEntryBindingType_Object=MibTableColumn
etsysAntiSpoofStationBindingEntryBindingType=_EtsysAntiSpoofStationBindingEntryBindingType_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1,1,11),_EtsysAntiSpoofStationBindingEntryBindingType_Type())
etsysAntiSpoofStationBindingEntryBindingType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryBindingType.setStatus(_A)
_EtsysAntiSpoofStationBindingEntryDurationTime_Type=Unsigned32
_EtsysAntiSpoofStationBindingEntryDurationTime_Object=MibTableColumn
etsysAntiSpoofStationBindingEntryDurationTime=_EtsysAntiSpoofStationBindingEntryDurationTime_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1,1,12),_EtsysAntiSpoofStationBindingEntryDurationTime_Type())
etsysAntiSpoofStationBindingEntryDurationTime.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryDurationTime.setStatus(_A)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryDurationTime.setUnits(_J)
_EtsysAntiSpoofStationBindingEntryExpirationTime_Type=Unsigned32
_EtsysAntiSpoofStationBindingEntryExpirationTime_Object=MibTableColumn
etsysAntiSpoofStationBindingEntryExpirationTime=_EtsysAntiSpoofStationBindingEntryExpirationTime_Object((1,3,6,1,4,1,5624,1,2,96,1,4,1,1,13),_EtsysAntiSpoofStationBindingEntryExpirationTime_Type())
etsysAntiSpoofStationBindingEntryExpirationTime.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryExpirationTime.setStatus(_A)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingEntryExpirationTime.setUnits(_J)
_EtsysAntiSpoofMacBindingTable_Object=MibTable
etsysAntiSpoofMacBindingTable=_EtsysAntiSpoofMacBindingTable_Object((1,3,6,1,4,1,5624,1,2,96,1,4,2))
if mibBuilder.loadTexts:etsysAntiSpoofMacBindingTable.setStatus(_A)
_EtsysAntiSpoofMacBindingEntry_Object=MibTableRow
etsysAntiSpoofMacBindingEntry=_EtsysAntiSpoofMacBindingEntry_Object((1,3,6,1,4,1,5624,1,2,96,1,4,2,1))
etsysAntiSpoofMacBindingEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_G),(0,_B,_L))
if mibBuilder.loadTexts:etsysAntiSpoofMacBindingEntry.setStatus(_A)
_EtsysAntiSpoofStationBindingInterface_Type=InterfaceIndexOrZero
_EtsysAntiSpoofStationBindingInterface_Object=MibTableColumn
etsysAntiSpoofStationBindingInterface=_EtsysAntiSpoofStationBindingInterface_Object((1,3,6,1,4,1,5624,1,2,96,1,4,2,1,1),_EtsysAntiSpoofStationBindingInterface_Type())
etsysAntiSpoofStationBindingInterface.setMaxAccess(_K)
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingInterface.setStatus(_A)
_EtsysAntiSpoofMacStationBindingIndex_Type=EtsysInstanceOID
_EtsysAntiSpoofMacStationBindingIndex_Object=MibTableColumn
etsysAntiSpoofMacStationBindingIndex=_EtsysAntiSpoofMacStationBindingIndex_Object((1,3,6,1,4,1,5624,1,2,96,1,4,2,1,2),_EtsysAntiSpoofMacStationBindingIndex_Type())
etsysAntiSpoofMacStationBindingIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofMacStationBindingIndex.setStatus(_A)
_EtsysAntiSpoofMacBindingClearBinding_Type=TruthValue
_EtsysAntiSpoofMacBindingClearBinding_Object=MibTableColumn
etsysAntiSpoofMacBindingClearBinding=_EtsysAntiSpoofMacBindingClearBinding_Object((1,3,6,1,4,1,5624,1,2,96,1,4,2,1,3),_EtsysAntiSpoofMacBindingClearBinding_Type())
etsysAntiSpoofMacBindingClearBinding.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofMacBindingClearBinding.setStatus(_A)
_EtsysAntiSpoofIpBindingTable_Object=MibTable
etsysAntiSpoofIpBindingTable=_EtsysAntiSpoofIpBindingTable_Object((1,3,6,1,4,1,5624,1,2,96,1,4,3))
if mibBuilder.loadTexts:etsysAntiSpoofIpBindingTable.setStatus(_A)
_EtsysAntiSpoofIpBindingEntry_Object=MibTableRow
etsysAntiSpoofIpBindingEntry=_EtsysAntiSpoofIpBindingEntry_Object((1,3,6,1,4,1,5624,1,2,96,1,4,3,1))
etsysAntiSpoofIpBindingEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_E),(0,_B,_L))
if mibBuilder.loadTexts:etsysAntiSpoofIpBindingEntry.setStatus(_A)
_EtsysAntiSpoofIpStationBindingIndex_Type=EtsysInstanceOID
_EtsysAntiSpoofIpStationBindingIndex_Object=MibTableColumn
etsysAntiSpoofIpStationBindingIndex=_EtsysAntiSpoofIpStationBindingIndex_Object((1,3,6,1,4,1,5624,1,2,96,1,4,3,1,1),_EtsysAntiSpoofIpStationBindingIndex_Type())
etsysAntiSpoofIpStationBindingIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofIpStationBindingIndex.setStatus(_A)
_EtsysAntiSpoofIpBindingClearBinding_Type=TruthValue
_EtsysAntiSpoofIpBindingClearBinding_Object=MibTableColumn
etsysAntiSpoofIpBindingClearBinding=_EtsysAntiSpoofIpBindingClearBinding_Object((1,3,6,1,4,1,5624,1,2,96,1,4,3,1,2),_EtsysAntiSpoofIpBindingClearBinding_Type())
etsysAntiSpoofIpBindingClearBinding.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofIpBindingClearBinding.setStatus(_A)
_EtsysAntiSpoofPortBindingTable_Object=MibTable
etsysAntiSpoofPortBindingTable=_EtsysAntiSpoofPortBindingTable_Object((1,3,6,1,4,1,5624,1,2,96,1,4,4))
if mibBuilder.loadTexts:etsysAntiSpoofPortBindingTable.setStatus(_A)
_EtsysAntiSpoofPortBindingEntry_Object=MibTableRow
etsysAntiSpoofPortBindingEntry=_EtsysAntiSpoofPortBindingEntry_Object((1,3,6,1,4,1,5624,1,2,96,1,4,4,1))
etsysAntiSpoofPortBindingEntry.setIndexNames((0,_B,_L),(0,_B,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:etsysAntiSpoofPortBindingEntry.setStatus(_A)
_EtsysAntiSpoofPortStationBindingIndex_Type=EtsysInstanceOID
_EtsysAntiSpoofPortStationBindingIndex_Object=MibTableColumn
etsysAntiSpoofPortStationBindingIndex=_EtsysAntiSpoofPortStationBindingIndex_Object((1,3,6,1,4,1,5624,1,2,96,1,4,4,1,1),_EtsysAntiSpoofPortStationBindingIndex_Type())
etsysAntiSpoofPortStationBindingIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysAntiSpoofPortStationBindingIndex.setStatus(_A)
_EtsysAntiSpoofPortBindingClearBinding_Type=TruthValue
_EtsysAntiSpoofPortBindingClearBinding_Object=MibTableColumn
etsysAntiSpoofPortBindingClearBinding=_EtsysAntiSpoofPortBindingClearBinding_Object((1,3,6,1,4,1,5624,1,2,96,1,4,4,1,2),_EtsysAntiSpoofPortBindingClearBinding_Type())
etsysAntiSpoofPortBindingClearBinding.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysAntiSpoofPortBindingClearBinding.setStatus(_A)
_EtsysAntiSpoofConformance_ObjectIdentity=ObjectIdentity
etsysAntiSpoofConformance=_EtsysAntiSpoofConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,96,2))
_EtsysAntiSpoofGroups_ObjectIdentity=ObjectIdentity
etsysAntiSpoofGroups=_EtsysAntiSpoofGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,96,2,1))
_EtsysAntiSpoofCompliances_ObjectIdentity=ObjectIdentity
etsysAntiSpoofCompliances=_EtsysAntiSpoofCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,96,2,2))
etsysAntiSpoofSystemGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,96,2,1,1))
etsysAntiSpoofSystemGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:etsysAntiSpoofSystemGroup.setStatus(_A)
etsysAntiSpoofClassGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,96,2,1,2))
etsysAntiSpoofClassGroup.setObjects(*((_B,_j),(_B,_k)))
if mibBuilder.loadTexts:etsysAntiSpoofClassGroup.setStatus(_A)
etsysAntiSpoofThresholdGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,96,2,1,3))
etsysAntiSpoofThresholdGroup.setObjects(*((_B,_S),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:etsysAntiSpoofThresholdGroup.setStatus(_A)
etsysAntiSpoofPortGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,96,2,1,4))
etsysAntiSpoofPortGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:etsysAntiSpoofPortGroup.setStatus(_A)
etsysAntiSpoofStationBindingGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,96,2,1,5))
etsysAntiSpoofStationBindingGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_v),(_B,_w),(_B,_M),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:etsysAntiSpoofStationBindingGroup.setStatus(_A)
etsysAntiSpoofMacBindingGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,96,2,1,6))
etsysAntiSpoofMacBindingGroup.setObjects(*((_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:etsysAntiSpoofMacBindingGroup.setStatus(_A)
etsysAntiSpoofIpBindingGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,96,2,1,7))
etsysAntiSpoofIpBindingGroup.setObjects(*((_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:etsysAntiSpoofIpBindingGroup.setStatus(_A)
etsysAntiSpoofPortBindingGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,96,2,1,8))
etsysAntiSpoofPortBindingGroup.setObjects(*((_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:etsysAntiSpoofPortBindingGroup.setStatus(_A)
etsysAntiSpoofClassNotification=NotificationType((1,3,6,1,4,1,5624,1,2,96,1,0,1))
etsysAntiSpoofClassNotification.setObjects(*((_B,_S),(_B,_E),(_B,_F),(_B,_G),(_B,_M)))
if mibBuilder.loadTexts:etsysAntiSpoofClassNotification.setStatus(_A)
etsysAntiSpoofDuplicateIpNotification=NotificationType((1,3,6,1,4,1,5624,1,2,96,1,0,2))
etsysAntiSpoofDuplicateIpNotification.setObjects(*((_B,_E),(_B,_M),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:etsysAntiSpoofDuplicateIpNotification.setStatus(_A)
etsysAntiSpoofNotificationGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,96,2,1,9))
etsysAntiSpoofNotificationGroup.setObjects(*((_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:etsysAntiSpoofNotificationGroup.setStatus(_A)
etsysAntiSpoofCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,96,2,2,1))
etsysAntiSpoofCompliance.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:etsysAntiSpoofCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AntiSpoofPortAction':AntiSpoofPortAction,_R:AntiSpoofInspectionType,'AntiSpoofThresholdType':AntiSpoofThresholdType,_Y:AntiSpoofPortType,'AntiSpoofBindingType':AntiSpoofBindingType,'EtsysInstanceOID':EtsysInstanceOID,'etsysAntiSpoofMIB':etsysAntiSpoofMIB,'etsysAntiSpoofObjects':etsysAntiSpoofObjects,'etsysAntiSpoofNotificationBranch':etsysAntiSpoofNotificationBranch,_A9:etsysAntiSpoofClassNotification,_AA:etsysAntiSpoofDuplicateIpNotification,'etsysAntiSpoofSystemBranch':etsysAntiSpoofSystemBranch,_a:etsysAntiSpoofSystemState,_b:etsysAntiSpoofMaxClassIndex,_c:etsysAntiSpoofMaxClassThresholdIndex,_d:etsysAntiSpoofSystemSnmpNotifications,_e:etsysAntiSpoofSystemNotificationInterval,_f:etsysAntiSpoofDuplicateIpControl,_g:etsysAntiSpoofSupportedActionTypes,_h:etsysAntiSpoofSupportedThresholdTypes,_i:etsysAntiSpoofSupportedBindingTypes,'etsysAntiSpoofClassBranch':etsysAntiSpoofClassBranch,'etsysAntiSpoofClassTable':etsysAntiSpoofClassTable,'etsysAntiSpoofClassEntry':etsysAntiSpoofClassEntry,_Q:etsysAntiSpoofClassIndex,_j:etsysAntiSpoofClassName,_k:etsysAntiSpoofClassTimeout,'etsysAntiSpoofThresholdTable':etsysAntiSpoofThresholdTable,'etsysAntiSpoofThresholdEntry':etsysAntiSpoofThresholdEntry,_X:etsysAntiSpoofThresholdIndex,_S:etsysAntiSpoofThresholdValue,_l:etsysAntiSpoofThresholdActionMask,_m:etsysAntiSpoofThresholdActionQuarantineValue,_n:etsysAntiSpoofThresholdType,'etsysAntiSpoofPortBranch':etsysAntiSpoofPortBranch,'etsysAntiSpoofPortConfigTable':etsysAntiSpoofPortConfigTable,'etsysAntiSpoofPortConfigEntry':etsysAntiSpoofPortConfigEntry,_o:etsysAntiSpoofDHCPMode,_p:etsysAntiSpoofDHCPMacVerify,_q:etsysAntiSpoofArpInspection,_r:etsysAntiSpoofIpInspection,_s:etsysAntiSpoofPortClassIndex,_t:etsysAntiSpoofUntrustedTrafficPacketCounter,'etsysAntiSpoofPortTypeTable':etsysAntiSpoofPortTypeTable,'etsysAntiSpoofPortTypeEntry':etsysAntiSpoofPortTypeEntry,_u:etsysAntiSpoofPortType,'etsysAntiSpoofBindingBranch':etsysAntiSpoofBindingBranch,'etsysAntiSpoofStationBindingTable':etsysAntiSpoofStationBindingTable,'etsysAntiSpoofStationBindingEntry':etsysAntiSpoofStationBindingEntry,_Z:etsysAntiSpoofStationBindingEntryIndex,_E:etsysAntiSpoofStationBindingEntryMacAddr,_F:etsysAntiSpoofStationBindingEntryInetAddrType,_G:etsysAntiSpoofStationBindingEntryInetAddr,_M:etsysAntiSpoofStationBindingEntryIfIndex,_v:etsysAntiSpoofStationBindingEntryInetCounter,_w:etsysAntiSpoofStationBindingEntryClearInetCounter,_x:etsysAntiSpoofStationBindingEntryPortCounter,_y:etsysAntiSpoofStationBindingEntryClearPortCounter,_z:etsysAntiSpoofStationBindingEntryClearBinding,_A0:etsysAntiSpoofStationBindingEntryBindingType,_A1:etsysAntiSpoofStationBindingEntryDurationTime,_A2:etsysAntiSpoofStationBindingEntryExpirationTime,'etsysAntiSpoofMacBindingTable':etsysAntiSpoofMacBindingTable,'etsysAntiSpoofMacBindingEntry':etsysAntiSpoofMacBindingEntry,_L:etsysAntiSpoofStationBindingInterface,_A3:etsysAntiSpoofMacStationBindingIndex,_A4:etsysAntiSpoofMacBindingClearBinding,'etsysAntiSpoofIpBindingTable':etsysAntiSpoofIpBindingTable,'etsysAntiSpoofIpBindingEntry':etsysAntiSpoofIpBindingEntry,_A5:etsysAntiSpoofIpStationBindingIndex,_A6:etsysAntiSpoofIpBindingClearBinding,'etsysAntiSpoofPortBindingTable':etsysAntiSpoofPortBindingTable,'etsysAntiSpoofPortBindingEntry':etsysAntiSpoofPortBindingEntry,_A7:etsysAntiSpoofPortStationBindingIndex,_A8:etsysAntiSpoofPortBindingClearBinding,'etsysAntiSpoofConformance':etsysAntiSpoofConformance,'etsysAntiSpoofGroups':etsysAntiSpoofGroups,_AB:etsysAntiSpoofSystemGroup,_AC:etsysAntiSpoofClassGroup,_AD:etsysAntiSpoofThresholdGroup,_AE:etsysAntiSpoofPortGroup,_AF:etsysAntiSpoofStationBindingGroup,_AG:etsysAntiSpoofMacBindingGroup,_AI:etsysAntiSpoofIpBindingGroup,_AH:etsysAntiSpoofPortBindingGroup,_AJ:etsysAntiSpoofNotificationGroup,'etsysAntiSpoofCompliances':etsysAntiSpoofCompliances,'etsysAntiSpoofCompliance':etsysAntiSpoofCompliance})