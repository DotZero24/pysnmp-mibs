_U='t11FLockActiveGroup'
_T='t11FLockRowStatus'
_S='t11FLockRejectReasonVendorCode'
_R='t11FLockRejectReasonCodeExp'
_Q='t11FLockRejectReasonCode'
_P='t11FLockStatus'
_O='t11FLockInitiatorIpAddr'
_N='t11FLockInitiatorIpAddrType'
_M='t11FLockInitiator'
_L='t11FLockInitiatorType'
_K='not-accessible'
_J='t11FLockApplicationID'
_I='t11FLockFabricIndex'
_H='fcmSwitchIndex'
_G='fcmInstanceIndex'
_F='Integer32'
_E='FC-MGMT-MIB'
_D='OctetString'
_C='read-only'
_B='T11-FC-FABRIC-LOCK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fcmInstanceIndex,fcmSwitchIndex=mibBuilder.importSymbols(_E,_G,_H)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
T11NsGs4RejectReasonCode,=mibBuilder.importSymbols('T11-FC-NAME-SERVER-MIB','T11NsGs4RejectReasonCode')
T11FabricIndex,=mibBuilder.importSymbols('T11-TC-MIB','T11FabricIndex')
t11FabricLockMIB=ModuleIdentity((1,3,6,1,2,1,159))
if mibBuilder.loadTexts:t11FabricLockMIB.setRevisions(('2007-06-27 00:00',))
_T11FLockMIBNotifications_ObjectIdentity=ObjectIdentity
t11FLockMIBNotifications=_T11FLockMIBNotifications_ObjectIdentity((1,3,6,1,2,1,159,0))
_T11FLockMIBObjects_ObjectIdentity=ObjectIdentity
t11FLockMIBObjects=_T11FLockMIBObjects_ObjectIdentity((1,3,6,1,2,1,159,1))
_T11FLockConfiguration_ObjectIdentity=ObjectIdentity
t11FLockConfiguration=_T11FLockConfiguration_ObjectIdentity((1,3,6,1,2,1,159,1,1))
_T11FLockTable_Object=MibTable
t11FLockTable=_T11FLockTable_Object((1,3,6,1,2,1,159,1,1,1))
if mibBuilder.loadTexts:t11FLockTable.setStatus(_A)
_T11FLockEntry_Object=MibTableRow
t11FLockEntry=_T11FLockEntry_Object((1,3,6,1,2,1,159,1,1,1,1))
t11FLockEntry.setIndexNames((0,_E,_G),(0,_E,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:t11FLockEntry.setStatus(_A)
_T11FLockFabricIndex_Type=T11FabricIndex
_T11FLockFabricIndex_Object=MibTableColumn
t11FLockFabricIndex=_T11FLockFabricIndex_Object((1,3,6,1,2,1,159,1,1,1,1,1),_T11FLockFabricIndex_Type())
t11FLockFabricIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:t11FLockFabricIndex.setStatus(_A)
class _T11FLockApplicationID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_T11FLockApplicationID_Type.__name__=_D
_T11FLockApplicationID_Object=MibTableColumn
t11FLockApplicationID=_T11FLockApplicationID_Object((1,3,6,1,2,1,159,1,1,1,1,2),_T11FLockApplicationID_Type())
t11FLockApplicationID.setMaxAccess(_K)
if mibBuilder.loadTexts:t11FLockApplicationID.setStatus(_A)
class _T11FLockInitiatorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ssb',2),('cli',3),('snmp',4)))
_T11FLockInitiatorType_Type.__name__=_F
_T11FLockInitiatorType_Object=MibTableColumn
t11FLockInitiatorType=_T11FLockInitiatorType_Object((1,3,6,1,2,1,159,1,1,1,1,3),_T11FLockInitiatorType_Type())
t11FLockInitiatorType.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FLockInitiatorType.setStatus(_A)
class _T11FLockInitiator_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_T11FLockInitiator_Type.__name__=_D
_T11FLockInitiator_Object=MibTableColumn
t11FLockInitiator=_T11FLockInitiator_Object((1,3,6,1,2,1,159,1,1,1,1,4),_T11FLockInitiator_Type())
t11FLockInitiator.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FLockInitiator.setStatus(_A)
_T11FLockInitiatorIpAddrType_Type=InetAddressType
_T11FLockInitiatorIpAddrType_Object=MibTableColumn
t11FLockInitiatorIpAddrType=_T11FLockInitiatorIpAddrType_Object((1,3,6,1,2,1,159,1,1,1,1,5),_T11FLockInitiatorIpAddrType_Type())
t11FLockInitiatorIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FLockInitiatorIpAddrType.setStatus(_A)
_T11FLockInitiatorIpAddr_Type=InetAddress
_T11FLockInitiatorIpAddr_Object=MibTableColumn
t11FLockInitiatorIpAddr=_T11FLockInitiatorIpAddr_Object((1,3,6,1,2,1,159,1,1,1,1,6),_T11FLockInitiatorIpAddr_Type())
t11FLockInitiatorIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FLockInitiatorIpAddr.setStatus(_A)
class _T11FLockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('settingUp',2),('rejectFailure',3),('otherFailure',4)))
_T11FLockStatus_Type.__name__=_F
_T11FLockStatus_Object=MibTableColumn
t11FLockStatus=_T11FLockStatus_Object((1,3,6,1,2,1,159,1,1,1,1,7),_T11FLockStatus_Type())
t11FLockStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FLockStatus.setStatus(_A)
_T11FLockRejectReasonCode_Type=T11NsGs4RejectReasonCode
_T11FLockRejectReasonCode_Object=MibTableColumn
t11FLockRejectReasonCode=_T11FLockRejectReasonCode_Object((1,3,6,1,2,1,159,1,1,1,1,8),_T11FLockRejectReasonCode_Type())
t11FLockRejectReasonCode.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FLockRejectReasonCode.setStatus(_A)
class _T11FLockRejectReasonCodeExp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,1))
_T11FLockRejectReasonCodeExp_Type.__name__=_D
_T11FLockRejectReasonCodeExp_Object=MibTableColumn
t11FLockRejectReasonCodeExp=_T11FLockRejectReasonCodeExp_Object((1,3,6,1,2,1,159,1,1,1,1,9),_T11FLockRejectReasonCodeExp_Type())
t11FLockRejectReasonCodeExp.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FLockRejectReasonCodeExp.setStatus(_A)
class _T11FLockRejectReasonVendorCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,1))
_T11FLockRejectReasonVendorCode_Type.__name__=_D
_T11FLockRejectReasonVendorCode_Object=MibTableColumn
t11FLockRejectReasonVendorCode=_T11FLockRejectReasonVendorCode_Object((1,3,6,1,2,1,159,1,1,1,1,10),_T11FLockRejectReasonVendorCode_Type())
t11FLockRejectReasonVendorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:t11FLockRejectReasonVendorCode.setStatus(_A)
_T11FLockRowStatus_Type=RowStatus
_T11FLockRowStatus_Object=MibTableColumn
t11FLockRowStatus=_T11FLockRowStatus_Object((1,3,6,1,2,1,159,1,1,1,1,11),_T11FLockRowStatus_Type())
t11FLockRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:t11FLockRowStatus.setStatus(_A)
_T11FLockMIBConformance_ObjectIdentity=ObjectIdentity
t11FLockMIBConformance=_T11FLockMIBConformance_ObjectIdentity((1,3,6,1,2,1,159,2))
_T11FLockMIBCompliances_ObjectIdentity=ObjectIdentity
t11FLockMIBCompliances=_T11FLockMIBCompliances_ObjectIdentity((1,3,6,1,2,1,159,2,1))
_T11FLockMIBGroups_ObjectIdentity=ObjectIdentity
t11FLockMIBGroups=_T11FLockMIBGroups_ObjectIdentity((1,3,6,1,2,1,159,2,2))
t11FLockActiveGroup=ObjectGroup((1,3,6,1,2,1,159,2,2,1))
t11FLockActiveGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:t11FLockActiveGroup.setStatus(_A)
t11FLockMIBCompliance=ModuleCompliance((1,3,6,1,2,1,159,2,1,1))
t11FLockMIBCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:t11FLockMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'t11FabricLockMIB':t11FabricLockMIB,'t11FLockMIBNotifications':t11FLockMIBNotifications,'t11FLockMIBObjects':t11FLockMIBObjects,'t11FLockConfiguration':t11FLockConfiguration,'t11FLockTable':t11FLockTable,'t11FLockEntry':t11FLockEntry,_I:t11FLockFabricIndex,_J:t11FLockApplicationID,_L:t11FLockInitiatorType,_M:t11FLockInitiator,_N:t11FLockInitiatorIpAddrType,_O:t11FLockInitiatorIpAddr,_P:t11FLockStatus,_Q:t11FLockRejectReasonCode,_R:t11FLockRejectReasonCodeExp,_S:t11FLockRejectReasonVendorCode,_T:t11FLockRowStatus,'t11FLockMIBConformance':t11FLockMIBConformance,'t11FLockMIBCompliances':t11FLockMIBCompliances,'t11FLockMIBCompliance':t11FLockMIBCompliance,'t11FLockMIBGroups':t11FLockMIBGroups,_U:t11FLockActiveGroup})