_j='etsysVrrpExtTrackedObjectGroup'
_i='etsysVrrpExtCriticalIpGroup'
_h='etsysVrrpExtOperGroup'
_g='etsysVrrpExtMIBGroup'
_f='etsysVrrpExtTrackedObjRowStatus'
_e='etsysVrrpExtTrackedObjState'
_d='etsysVrrpExtTrackedObjPriority'
_c='etsysVrrpExtCriticalIpAddrProbeName'
_b='etsysVrrpExtCriticalIpAddrProbe'
_a='etsysVrrpExtOperFabricRouteMode'
_Z='deprecated'
_Y='etsysVrrpExtTrackedObjName'
_X='etsysVrrpExtCriticalIpAddr'
_W='vrrpOperationsInetAddrType'
_V='VRRP-MIB'
_U='InetAddress'
_T='etsysVrrpExtCriticalIpAddrRowStatus'
_S='etsysVrrpExtCriticalIpAddrState'
_R='etsysVrrpExtCriticalIpAddrPriority'
_Q='etsysVrrpExtOperCriticalIpAddrCount'
_P='etsysVrrpExtOperPreemptModeDelay'
_O='etsysVrrpExtOperAcceptMode'
_N='etsysVrrpExtOperState'
_M='read-write'
_L='disable'
_K='enable'
_J='read-only'
_I='not-accessible'
_H='SnmpAdminString'
_G='etsysVrrpExtOperVrId'
_F='ifIndex'
_E='IF-MIB'
_D='read-create'
_C='Integer32'
_B='current'
_A='ENTERASYS-VRRP-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_U,'InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
VrId,vrrpOperationsInetAddrType=mibBuilder.importSymbols(_V,'VrId',_W)
etsysVrrpExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,64))
if mibBuilder.loadTexts:etsysVrrpExtMIB.setRevisions(('2011-10-27 14:29','2009-08-10 19:43'))
_EtsysVrrpExtOperations_ObjectIdentity=ObjectIdentity
etsysVrrpExtOperations=_EtsysVrrpExtOperations_ObjectIdentity((1,3,6,1,4,1,5624,1,2,64,1))
_EtsysVrrpExtOperTable_Object=MibTable
etsysVrrpExtOperTable=_EtsysVrrpExtOperTable_Object((1,3,6,1,4,1,5624,1,2,64,1,1))
if mibBuilder.loadTexts:etsysVrrpExtOperTable.setStatus(_B)
_EtsysVrrpExtOperEntry_Object=MibTableRow
etsysVrrpExtOperEntry=_EtsysVrrpExtOperEntry_Object((1,3,6,1,4,1,5624,1,2,64,1,1,1))
etsysVrrpExtOperEntry.setIndexNames((0,_E,_F),(0,_A,_G))
if mibBuilder.loadTexts:etsysVrrpExtOperEntry.setStatus(_B)
_EtsysVrrpExtOperVrId_Type=VrId
_EtsysVrrpExtOperVrId_Object=MibTableColumn
etsysVrrpExtOperVrId=_EtsysVrrpExtOperVrId_Object((1,3,6,1,4,1,5624,1,2,64,1,1,1,1),_EtsysVrrpExtOperVrId_Type())
etsysVrrpExtOperVrId.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysVrrpExtOperVrId.setStatus(_B)
class _EtsysVrrpExtOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('initialize',1),('backup',2),('master',3),('ifDown',4),('preemptDelay',5)))
_EtsysVrrpExtOperState_Type.__name__=_C
_EtsysVrrpExtOperState_Object=MibTableColumn
etsysVrrpExtOperState=_EtsysVrrpExtOperState_Object((1,3,6,1,4,1,5624,1,2,64,1,1,1,2),_EtsysVrrpExtOperState_Type())
etsysVrrpExtOperState.setMaxAccess(_J)
if mibBuilder.loadTexts:etsysVrrpExtOperState.setStatus(_B)
class _EtsysVrrpExtOperAcceptMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_EtsysVrrpExtOperAcceptMode_Type.__name__=_C
_EtsysVrrpExtOperAcceptMode_Object=MibTableColumn
etsysVrrpExtOperAcceptMode=_EtsysVrrpExtOperAcceptMode_Object((1,3,6,1,4,1,5624,1,2,64,1,1,1,3),_EtsysVrrpExtOperAcceptMode_Type())
etsysVrrpExtOperAcceptMode.setMaxAccess(_M)
if mibBuilder.loadTexts:etsysVrrpExtOperAcceptMode.setStatus(_B)
class _EtsysVrrpExtOperPreemptModeDelay_Type(Integer32):defaultValue=0
_EtsysVrrpExtOperPreemptModeDelay_Type.__name__=_C
_EtsysVrrpExtOperPreemptModeDelay_Object=MibTableColumn
etsysVrrpExtOperPreemptModeDelay=_EtsysVrrpExtOperPreemptModeDelay_Object((1,3,6,1,4,1,5624,1,2,64,1,1,1,4),_EtsysVrrpExtOperPreemptModeDelay_Type())
etsysVrrpExtOperPreemptModeDelay.setMaxAccess(_M)
if mibBuilder.loadTexts:etsysVrrpExtOperPreemptModeDelay.setStatus(_B)
_EtsysVrrpExtOperCriticalIpAddrCount_Type=Integer32
_EtsysVrrpExtOperCriticalIpAddrCount_Object=MibTableColumn
etsysVrrpExtOperCriticalIpAddrCount=_EtsysVrrpExtOperCriticalIpAddrCount_Object((1,3,6,1,4,1,5624,1,2,64,1,1,1,5),_EtsysVrrpExtOperCriticalIpAddrCount_Type())
etsysVrrpExtOperCriticalIpAddrCount.setMaxAccess(_J)
if mibBuilder.loadTexts:etsysVrrpExtOperCriticalIpAddrCount.setStatus(_B)
class _EtsysVrrpExtOperFabricRouteMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_EtsysVrrpExtOperFabricRouteMode_Type.__name__=_C
_EtsysVrrpExtOperFabricRouteMode_Object=MibTableColumn
etsysVrrpExtOperFabricRouteMode=_EtsysVrrpExtOperFabricRouteMode_Object((1,3,6,1,4,1,5624,1,2,64,1,1,1,6),_EtsysVrrpExtOperFabricRouteMode_Type())
etsysVrrpExtOperFabricRouteMode.setMaxAccess(_M)
if mibBuilder.loadTexts:etsysVrrpExtOperFabricRouteMode.setStatus(_B)
_EtsysVrrpExtCriticalIpAddrTable_Object=MibTable
etsysVrrpExtCriticalIpAddrTable=_EtsysVrrpExtCriticalIpAddrTable_Object((1,3,6,1,4,1,5624,1,2,64,1,2))
if mibBuilder.loadTexts:etsysVrrpExtCriticalIpAddrTable.setStatus(_B)
_EtsysVrrpExtCriticalIpAddrEntry_Object=MibTableRow
etsysVrrpExtCriticalIpAddrEntry=_EtsysVrrpExtCriticalIpAddrEntry_Object((1,3,6,1,4,1,5624,1,2,64,1,2,1))
etsysVrrpExtCriticalIpAddrEntry.setIndexNames((0,_E,_F),(0,_A,_G),(0,_V,_W),(0,_A,_X))
if mibBuilder.loadTexts:etsysVrrpExtCriticalIpAddrEntry.setStatus(_B)
class _EtsysVrrpExtCriticalIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_EtsysVrrpExtCriticalIpAddr_Type.__name__=_U
_EtsysVrrpExtCriticalIpAddr_Object=MibTableColumn
etsysVrrpExtCriticalIpAddr=_EtsysVrrpExtCriticalIpAddr_Object((1,3,6,1,4,1,5624,1,2,64,1,2,1,1),_EtsysVrrpExtCriticalIpAddr_Type())
etsysVrrpExtCriticalIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysVrrpExtCriticalIpAddr.setStatus(_B)
class _EtsysVrrpExtCriticalIpAddrPriority_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_EtsysVrrpExtCriticalIpAddrPriority_Type.__name__=_C
_EtsysVrrpExtCriticalIpAddrPriority_Object=MibTableColumn
etsysVrrpExtCriticalIpAddrPriority=_EtsysVrrpExtCriticalIpAddrPriority_Object((1,3,6,1,4,1,5624,1,2,64,1,2,1,2),_EtsysVrrpExtCriticalIpAddrPriority_Type())
etsysVrrpExtCriticalIpAddrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVrrpExtCriticalIpAddrPriority.setStatus(_B)
class _EtsysVrrpExtCriticalIpAddrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_EtsysVrrpExtCriticalIpAddrState_Type.__name__=_C
_EtsysVrrpExtCriticalIpAddrState_Object=MibTableColumn
etsysVrrpExtCriticalIpAddrState=_EtsysVrrpExtCriticalIpAddrState_Object((1,3,6,1,4,1,5624,1,2,64,1,2,1,3),_EtsysVrrpExtCriticalIpAddrState_Type())
etsysVrrpExtCriticalIpAddrState.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVrrpExtCriticalIpAddrState.setStatus(_B)
_EtsysVrrpExtCriticalIpAddrRowStatus_Type=RowStatus
_EtsysVrrpExtCriticalIpAddrRowStatus_Object=MibTableColumn
etsysVrrpExtCriticalIpAddrRowStatus=_EtsysVrrpExtCriticalIpAddrRowStatus_Object((1,3,6,1,4,1,5624,1,2,64,1,2,1,4),_EtsysVrrpExtCriticalIpAddrRowStatus_Type())
etsysVrrpExtCriticalIpAddrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVrrpExtCriticalIpAddrRowStatus.setStatus(_B)
class _EtsysVrrpExtCriticalIpAddrProbe_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_EtsysVrrpExtCriticalIpAddrProbe_Type.__name__=_C
_EtsysVrrpExtCriticalIpAddrProbe_Object=MibTableColumn
etsysVrrpExtCriticalIpAddrProbe=_EtsysVrrpExtCriticalIpAddrProbe_Object((1,3,6,1,4,1,5624,1,2,64,1,2,1,5),_EtsysVrrpExtCriticalIpAddrProbe_Type())
etsysVrrpExtCriticalIpAddrProbe.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVrrpExtCriticalIpAddrProbe.setStatus(_B)
class _EtsysVrrpExtCriticalIpAddrProbeName_Type(SnmpAdminString):defaultValue=OctetString('$vrrp_default');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_EtsysVrrpExtCriticalIpAddrProbeName_Type.__name__=_H
_EtsysVrrpExtCriticalIpAddrProbeName_Object=MibTableColumn
etsysVrrpExtCriticalIpAddrProbeName=_EtsysVrrpExtCriticalIpAddrProbeName_Object((1,3,6,1,4,1,5624,1,2,64,1,2,1,6),_EtsysVrrpExtCriticalIpAddrProbeName_Type())
etsysVrrpExtCriticalIpAddrProbeName.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVrrpExtCriticalIpAddrProbeName.setStatus(_B)
_EtsysVrrpExtTrackedObjTable_Object=MibTable
etsysVrrpExtTrackedObjTable=_EtsysVrrpExtTrackedObjTable_Object((1,3,6,1,4,1,5624,1,2,64,1,3))
if mibBuilder.loadTexts:etsysVrrpExtTrackedObjTable.setStatus(_B)
_EtsysVrrpExtTrackedObjEntry_Object=MibTableRow
etsysVrrpExtTrackedObjEntry=_EtsysVrrpExtTrackedObjEntry_Object((1,3,6,1,4,1,5624,1,2,64,1,3,1))
etsysVrrpExtTrackedObjEntry.setIndexNames((0,_E,_F),(0,_A,_G),(0,_A,_Y))
if mibBuilder.loadTexts:etsysVrrpExtTrackedObjEntry.setStatus(_B)
class _EtsysVrrpExtTrackedObjName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_EtsysVrrpExtTrackedObjName_Type.__name__=_H
_EtsysVrrpExtTrackedObjName_Object=MibTableColumn
etsysVrrpExtTrackedObjName=_EtsysVrrpExtTrackedObjName_Object((1,3,6,1,4,1,5624,1,2,64,1,3,1,1),_EtsysVrrpExtTrackedObjName_Type())
etsysVrrpExtTrackedObjName.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysVrrpExtTrackedObjName.setStatus(_B)
class _EtsysVrrpExtTrackedObjPriority_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_EtsysVrrpExtTrackedObjPriority_Type.__name__=_C
_EtsysVrrpExtTrackedObjPriority_Object=MibTableColumn
etsysVrrpExtTrackedObjPriority=_EtsysVrrpExtTrackedObjPriority_Object((1,3,6,1,4,1,5624,1,2,64,1,3,1,2),_EtsysVrrpExtTrackedObjPriority_Type())
etsysVrrpExtTrackedObjPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVrrpExtTrackedObjPriority.setStatus(_B)
class _EtsysVrrpExtTrackedObjState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_EtsysVrrpExtTrackedObjState_Type.__name__=_C
_EtsysVrrpExtTrackedObjState_Object=MibTableColumn
etsysVrrpExtTrackedObjState=_EtsysVrrpExtTrackedObjState_Object((1,3,6,1,4,1,5624,1,2,64,1,3,1,3),_EtsysVrrpExtTrackedObjState_Type())
etsysVrrpExtTrackedObjState.setMaxAccess(_J)
if mibBuilder.loadTexts:etsysVrrpExtTrackedObjState.setStatus(_B)
_EtsysVrrpExtTrackedObjRowStatus_Type=RowStatus
_EtsysVrrpExtTrackedObjRowStatus_Object=MibTableColumn
etsysVrrpExtTrackedObjRowStatus=_EtsysVrrpExtTrackedObjRowStatus_Object((1,3,6,1,4,1,5624,1,2,64,1,3,1,4),_EtsysVrrpExtTrackedObjRowStatus_Type())
etsysVrrpExtTrackedObjRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVrrpExtTrackedObjRowStatus.setStatus(_B)
_EtsysVrrpExtConformance_ObjectIdentity=ObjectIdentity
etsysVrrpExtConformance=_EtsysVrrpExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,64,2))
_EtsysVrrpExtMIBCompliances_ObjectIdentity=ObjectIdentity
etsysVrrpExtMIBCompliances=_EtsysVrrpExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,64,2,1))
_EtsysVrrpExtMIBGroups_ObjectIdentity=ObjectIdentity
etsysVrrpExtMIBGroups=_EtsysVrrpExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,64,2,2))
etsysVrrpExtMIBGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,64,2,2,1))
etsysVrrpExtMIBGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:etsysVrrpExtMIBGroup.setStatus(_Z)
etsysVrrpExtOperGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,64,2,2,2))
etsysVrrpExtOperGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_a)))
if mibBuilder.loadTexts:etsysVrrpExtOperGroup.setStatus(_B)
etsysVrrpExtCriticalIpGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,64,2,2,3))
etsysVrrpExtCriticalIpGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:etsysVrrpExtCriticalIpGroup.setStatus(_B)
etsysVrrpExtTrackedObjectGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,64,2,2,4))
etsysVrrpExtTrackedObjectGroup.setObjects(*((_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:etsysVrrpExtTrackedObjectGroup.setStatus(_B)
etsysVrrpExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,64,2,1,1))
etsysVrrpExtMIBCompliance.setObjects((_A,_g))
if mibBuilder.loadTexts:etsysVrrpExtMIBCompliance.setStatus(_Z)
etsysVrrpExtMIBv2Compliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,64,2,1,2))
etsysVrrpExtMIBv2Compliance.setObjects(*((_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:etsysVrrpExtMIBv2Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'etsysVrrpExtMIB':etsysVrrpExtMIB,'etsysVrrpExtOperations':etsysVrrpExtOperations,'etsysVrrpExtOperTable':etsysVrrpExtOperTable,'etsysVrrpExtOperEntry':etsysVrrpExtOperEntry,_G:etsysVrrpExtOperVrId,_N:etsysVrrpExtOperState,_O:etsysVrrpExtOperAcceptMode,_P:etsysVrrpExtOperPreemptModeDelay,_Q:etsysVrrpExtOperCriticalIpAddrCount,_a:etsysVrrpExtOperFabricRouteMode,'etsysVrrpExtCriticalIpAddrTable':etsysVrrpExtCriticalIpAddrTable,'etsysVrrpExtCriticalIpAddrEntry':etsysVrrpExtCriticalIpAddrEntry,_X:etsysVrrpExtCriticalIpAddr,_R:etsysVrrpExtCriticalIpAddrPriority,_S:etsysVrrpExtCriticalIpAddrState,_T:etsysVrrpExtCriticalIpAddrRowStatus,_b:etsysVrrpExtCriticalIpAddrProbe,_c:etsysVrrpExtCriticalIpAddrProbeName,'etsysVrrpExtTrackedObjTable':etsysVrrpExtTrackedObjTable,'etsysVrrpExtTrackedObjEntry':etsysVrrpExtTrackedObjEntry,_Y:etsysVrrpExtTrackedObjName,_d:etsysVrrpExtTrackedObjPriority,_e:etsysVrrpExtTrackedObjState,_f:etsysVrrpExtTrackedObjRowStatus,'etsysVrrpExtConformance':etsysVrrpExtConformance,'etsysVrrpExtMIBCompliances':etsysVrrpExtMIBCompliances,'etsysVrrpExtMIBCompliance':etsysVrrpExtMIBCompliance,'etsysVrrpExtMIBv2Compliance':etsysVrrpExtMIBv2Compliance,'etsysVrrpExtMIBGroups':etsysVrrpExtMIBGroups,_g:etsysVrrpExtMIBGroup,_h:etsysVrrpExtOperGroup,_i:etsysVrrpExtCriticalIpGroup,_j:etsysVrrpExtTrackedObjectGroup})