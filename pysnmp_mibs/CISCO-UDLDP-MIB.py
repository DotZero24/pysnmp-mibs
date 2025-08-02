_o='ciscoUdldpFastHelloNotificationGroup'
_n='ciscoUdldpFastHelloGroup'
_m='ciscoUdldpAggreModeOptionalGroup'
_l='cudldpFastHelloStatusChangeNotification'
_k='cudldpFastHelloLinkFailRptNotification'
_j='cudldpFastHelloOperationalPorts'
_i='cudldpFastHelloConfigPorts'
_h='cudldpFastHelloMaxPorts'
_g='cudldpFastHelloStatusChangeNotifEnable'
_f='cudldpFastHelloLinkFailRptNotifEnable'
_e='cudldpFastHelloErrorReportEnable'
_d='cudldpHelloIntervalExt'
_c='cudldpInterfaceOperMode'
_b='cudldpInterfaceAdminMode'
_a='cudldpGlobalMode'
_Z='cudldpInterfaceAggressiveMode'
_Y='cudldpInterfaceEnable'
_X='cudldpGlobalEnable'
_W='milliseconds'
_V='seconds'
_U='Unsigned32'
_T='ifIndex'
_S='ciscoUdldpMIBGroup3'
_R='ciscoUdldpMIBGroup'
_Q='cudldpIfFastHelloOperStatus'
_P='cudldpIfOperHelloInterval'
_O='cudldpIfFastHelloInterval'
_N='cudldpInterfaceOperStatus'
_M='aggressive'
_L='disable'
_K='enable'
_J='ifName'
_I='ciscoUdldpMIBGroup2'
_H='cudldpHelloInterval'
_G='IF-MIB'
_F='read-only'
_E='Integer32'
_D='deprecated'
_C='read-write'
_B='current'
_A='CISCO-UDLDP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,ifName=mibBuilder.importSymbols(_G,_T,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_U,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoUdldpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,118))
if mibBuilder.loadTexts:ciscoUdldpMIB.setRevisions(('2009-11-09 09:00','2007-11-27 00:00','2003-02-21 00:00','2002-10-10 00:00','2000-04-10 00:00','1998-11-10 00:00'))
_CiscoUdldpMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoUdldpMIBNotifs=_CiscoUdldpMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,118,0))
_CiscoUdldpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoUdldpMIBObjects=_CiscoUdldpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,118,1))
_CudldpGlobal_ObjectIdentity=ObjectIdentity
cudldpGlobal=_CudldpGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,118,1,1))
_CudldpGlobalEnable_Type=TruthValue
_CudldpGlobalEnable_Object=MibScalar
cudldpGlobalEnable=_CudldpGlobalEnable_Object((1,3,6,1,4,1,9,9,118,1,1,1),_CudldpGlobalEnable_Type())
cudldpGlobalEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cudldpGlobalEnable.setStatus(_D)
class _CudldpHelloInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7,90))
_CudldpHelloInterval_Type.__name__=_E
_CudldpHelloInterval_Object=MibScalar
cudldpHelloInterval=_CudldpHelloInterval_Object((1,3,6,1,4,1,9,9,118,1,1,2),_CudldpHelloInterval_Type())
cudldpHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cudldpHelloInterval.setStatus(_B)
if mibBuilder.loadTexts:cudldpHelloInterval.setUnits(_V)
class _CudldpGlobalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_CudldpGlobalMode_Type.__name__=_E
_CudldpGlobalMode_Object=MibScalar
cudldpGlobalMode=_CudldpGlobalMode_Object((1,3,6,1,4,1,9,9,118,1,1,3),_CudldpGlobalMode_Type())
cudldpGlobalMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cudldpGlobalMode.setStatus(_B)
class _CudldpHelloIntervalExt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,90))
_CudldpHelloIntervalExt_Type.__name__=_U
_CudldpHelloIntervalExt_Object=MibScalar
cudldpHelloIntervalExt=_CudldpHelloIntervalExt_Object((1,3,6,1,4,1,9,9,118,1,1,4),_CudldpHelloIntervalExt_Type())
cudldpHelloIntervalExt.setMaxAccess(_C)
if mibBuilder.loadTexts:cudldpHelloIntervalExt.setStatus(_B)
if mibBuilder.loadTexts:cudldpHelloIntervalExt.setUnits(_V)
_CudldpFastHelloLinkFailRptNotifEnable_Type=TruthValue
_CudldpFastHelloLinkFailRptNotifEnable_Object=MibScalar
cudldpFastHelloLinkFailRptNotifEnable=_CudldpFastHelloLinkFailRptNotifEnable_Object((1,3,6,1,4,1,9,9,118,1,1,5),_CudldpFastHelloLinkFailRptNotifEnable_Type())
cudldpFastHelloLinkFailRptNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cudldpFastHelloLinkFailRptNotifEnable.setStatus(_B)
_CudldpFastHelloStatusChangeNotifEnable_Type=TruthValue
_CudldpFastHelloStatusChangeNotifEnable_Object=MibScalar
cudldpFastHelloStatusChangeNotifEnable=_CudldpFastHelloStatusChangeNotifEnable_Object((1,3,6,1,4,1,9,9,118,1,1,6),_CudldpFastHelloStatusChangeNotifEnable_Type())
cudldpFastHelloStatusChangeNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cudldpFastHelloStatusChangeNotifEnable.setStatus(_B)
_CudldpInterface_ObjectIdentity=ObjectIdentity
cudldpInterface=_CudldpInterface_ObjectIdentity((1,3,6,1,4,1,9,9,118,1,2))
_CudldpInterfaceTable_Object=MibTable
cudldpInterfaceTable=_CudldpInterfaceTable_Object((1,3,6,1,4,1,9,9,118,1,2,1))
if mibBuilder.loadTexts:cudldpInterfaceTable.setStatus(_B)
_CudldpInterfaceEntry_Object=MibTableRow
cudldpInterfaceEntry=_CudldpInterfaceEntry_Object((1,3,6,1,4,1,9,9,118,1,2,1,1))
cudldpInterfaceEntry.setIndexNames((0,_G,_T))
if mibBuilder.loadTexts:cudldpInterfaceEntry.setStatus(_B)
_CudldpInterfaceEnable_Type=TruthValue
_CudldpInterfaceEnable_Object=MibTableColumn
cudldpInterfaceEnable=_CudldpInterfaceEnable_Object((1,3,6,1,4,1,9,9,118,1,2,1,1,1),_CudldpInterfaceEnable_Type())
cudldpInterfaceEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cudldpInterfaceEnable.setStatus(_D)
class _CudldpInterfaceOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('shutdown',1),('indeterminant',2),('biDirectional',3),('notApplicable',4)))
_CudldpInterfaceOperStatus_Type.__name__=_E
_CudldpInterfaceOperStatus_Object=MibTableColumn
cudldpInterfaceOperStatus=_CudldpInterfaceOperStatus_Object((1,3,6,1,4,1,9,9,118,1,2,1,1,2),_CudldpInterfaceOperStatus_Type())
cudldpInterfaceOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cudldpInterfaceOperStatus.setStatus(_B)
_CudldpInterfaceAggressiveMode_Type=TruthValue
_CudldpInterfaceAggressiveMode_Object=MibTableColumn
cudldpInterfaceAggressiveMode=_CudldpInterfaceAggressiveMode_Object((1,3,6,1,4,1,9,9,118,1,2,1,1,3),_CudldpInterfaceAggressiveMode_Type())
cudldpInterfaceAggressiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cudldpInterfaceAggressiveMode.setStatus(_D)
class _CudldpInterfaceAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),('default',4)))
_CudldpInterfaceAdminMode_Type.__name__=_E
_CudldpInterfaceAdminMode_Object=MibTableColumn
cudldpInterfaceAdminMode=_CudldpInterfaceAdminMode_Object((1,3,6,1,4,1,9,9,118,1,2,1,1,4),_CudldpInterfaceAdminMode_Type())
cudldpInterfaceAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cudldpInterfaceAdminMode.setStatus(_B)
class _CudldpInterfaceOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3)))
_CudldpInterfaceOperMode_Type.__name__=_E
_CudldpInterfaceOperMode_Object=MibTableColumn
cudldpInterfaceOperMode=_CudldpInterfaceOperMode_Object((1,3,6,1,4,1,9,9,118,1,2,1,1,5),_CudldpInterfaceOperMode_Type())
cudldpInterfaceOperMode.setMaxAccess(_F)
if mibBuilder.loadTexts:cudldpInterfaceOperMode.setStatus(_B)
_CudldpIfFastHelloInterval_Type=Unsigned32
_CudldpIfFastHelloInterval_Object=MibTableColumn
cudldpIfFastHelloInterval=_CudldpIfFastHelloInterval_Object((1,3,6,1,4,1,9,9,118,1,2,1,1,6),_CudldpIfFastHelloInterval_Type())
cudldpIfFastHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cudldpIfFastHelloInterval.setStatus(_B)
if mibBuilder.loadTexts:cudldpIfFastHelloInterval.setUnits(_W)
_CudldpIfOperHelloInterval_Type=Unsigned32
_CudldpIfOperHelloInterval_Object=MibTableColumn
cudldpIfOperHelloInterval=_CudldpIfOperHelloInterval_Object((1,3,6,1,4,1,9,9,118,1,2,1,1,7),_CudldpIfOperHelloInterval_Type())
cudldpIfOperHelloInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:cudldpIfOperHelloInterval.setStatus(_B)
if mibBuilder.loadTexts:cudldpIfOperHelloInterval.setUnits(_W)
class _CudldpIfFastHelloOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('operational',1),('notOperational',2)))
_CudldpIfFastHelloOperStatus_Type.__name__=_E
_CudldpIfFastHelloOperStatus_Object=MibTableColumn
cudldpIfFastHelloOperStatus=_CudldpIfFastHelloOperStatus_Object((1,3,6,1,4,1,9,9,118,1,2,1,1,8),_CudldpIfFastHelloOperStatus_Type())
cudldpIfFastHelloOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cudldpIfFastHelloOperStatus.setStatus(_B)
_CudldpFastHello_ObjectIdentity=ObjectIdentity
cudldpFastHello=_CudldpFastHello_ObjectIdentity((1,3,6,1,4,1,9,9,118,1,3))
_CudldpFastHelloErrorReportEnable_Type=TruthValue
_CudldpFastHelloErrorReportEnable_Object=MibScalar
cudldpFastHelloErrorReportEnable=_CudldpFastHelloErrorReportEnable_Object((1,3,6,1,4,1,9,9,118,1,3,1),_CudldpFastHelloErrorReportEnable_Type())
cudldpFastHelloErrorReportEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cudldpFastHelloErrorReportEnable.setStatus(_B)
_CudldpFastHelloMaxPorts_Type=Unsigned32
_CudldpFastHelloMaxPorts_Object=MibScalar
cudldpFastHelloMaxPorts=_CudldpFastHelloMaxPorts_Object((1,3,6,1,4,1,9,9,118,1,3,2),_CudldpFastHelloMaxPorts_Type())
cudldpFastHelloMaxPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:cudldpFastHelloMaxPorts.setStatus(_B)
_CudldpFastHelloConfigPorts_Type=Unsigned32
_CudldpFastHelloConfigPorts_Object=MibScalar
cudldpFastHelloConfigPorts=_CudldpFastHelloConfigPorts_Object((1,3,6,1,4,1,9,9,118,1,3,3),_CudldpFastHelloConfigPorts_Type())
cudldpFastHelloConfigPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:cudldpFastHelloConfigPorts.setStatus(_B)
_CudldpFastHelloOperationalPorts_Type=Unsigned32
_CudldpFastHelloOperationalPorts_Object=MibScalar
cudldpFastHelloOperationalPorts=_CudldpFastHelloOperationalPorts_Object((1,3,6,1,4,1,9,9,118,1,3,4),_CudldpFastHelloOperationalPorts_Type())
cudldpFastHelloOperationalPorts.setMaxAccess(_F)
if mibBuilder.loadTexts:cudldpFastHelloOperationalPorts.setStatus(_B)
_CiscoUdldpMIBConformance_ObjectIdentity=ObjectIdentity
ciscoUdldpMIBConformance=_CiscoUdldpMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,118,3))
_CiscoUdldpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoUdldpMIBCompliances=_CiscoUdldpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,118,3,1))
_CiscoUdldpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoUdldpMIBGroups=_CiscoUdldpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,118,3,2))
ciscoUdldpMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,118,3,2,1))
ciscoUdldpMIBGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_N)))
if mibBuilder.loadTexts:ciscoUdldpMIBGroup.setStatus(_D)
ciscoUdldpAggreModeOptionalGroup=ObjectGroup((1,3,6,1,4,1,9,9,118,3,2,2))
ciscoUdldpAggreModeOptionalGroup.setObjects(*((_A,_Z),(_A,_H)))
if mibBuilder.loadTexts:ciscoUdldpAggreModeOptionalGroup.setStatus(_D)
ciscoUdldpMIBGroup2=ObjectGroup((1,3,6,1,4,1,9,9,118,3,2,3))
ciscoUdldpMIBGroup2.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_H),(_A,_N)))
if mibBuilder.loadTexts:ciscoUdldpMIBGroup2.setStatus(_B)
ciscoUdldpMIBGroup3=ObjectGroup((1,3,6,1,4,1,9,9,118,3,2,4))
ciscoUdldpMIBGroup3.setObjects((_A,_d))
if mibBuilder.loadTexts:ciscoUdldpMIBGroup3.setStatus(_B)
ciscoUdldpFastHelloGroup=ObjectGroup((1,3,6,1,4,1,9,9,118,3,2,5))
ciscoUdldpFastHelloGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ciscoUdldpFastHelloGroup.setStatus(_B)
cudldpFastHelloLinkFailRptNotification=NotificationType((1,3,6,1,4,1,9,9,118,0,1))
cudldpFastHelloLinkFailRptNotification.setObjects((_G,_J))
if mibBuilder.loadTexts:cudldpFastHelloLinkFailRptNotification.setStatus(_B)
cudldpFastHelloStatusChangeNotification=NotificationType((1,3,6,1,4,1,9,9,118,0,2))
cudldpFastHelloStatusChangeNotification.setObjects(*((_A,_H),(_A,_O),(_A,_P),(_A,_Q),(_G,_J)))
if mibBuilder.loadTexts:cudldpFastHelloStatusChangeNotification.setStatus(_B)
ciscoUdldpFastHelloNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,118,3,2,6))
ciscoUdldpFastHelloNotificationGroup.setObjects(*((_A,_k),(_A,_l)))
if mibBuilder.loadTexts:ciscoUdldpFastHelloNotificationGroup.setStatus(_B)
ciscoUdldpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,118,3,1,1))
ciscoUdldpMIBCompliance.setObjects((_A,_R))
if mibBuilder.loadTexts:ciscoUdldpMIBCompliance.setStatus(_D)
ciscoUdldpMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,118,3,1,2))
ciscoUdldpMIBComplianceRev1.setObjects(*((_A,_R),(_A,_m)))
if mibBuilder.loadTexts:ciscoUdldpMIBComplianceRev1.setStatus(_D)
ciscoUdldpMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,118,3,1,3))
ciscoUdldpMIBComplianceRev2.setObjects((_A,_I))
if mibBuilder.loadTexts:ciscoUdldpMIBComplianceRev2.setStatus(_D)
ciscoUdldpMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,118,3,1,4))
ciscoUdldpMIBComplianceRev3.setObjects(*((_A,_I),(_A,_S)))
if mibBuilder.loadTexts:ciscoUdldpMIBComplianceRev3.setStatus(_D)
ciscoUdldpMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,118,3,1,5))
ciscoUdldpMIBComplianceRev4.setObjects(*((_A,_I),(_A,_S),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:ciscoUdldpMIBComplianceRev4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoUdldpMIB':ciscoUdldpMIB,'ciscoUdldpMIBNotifs':ciscoUdldpMIBNotifs,_k:cudldpFastHelloLinkFailRptNotification,_l:cudldpFastHelloStatusChangeNotification,'ciscoUdldpMIBObjects':ciscoUdldpMIBObjects,'cudldpGlobal':cudldpGlobal,_X:cudldpGlobalEnable,_H:cudldpHelloInterval,_a:cudldpGlobalMode,_d:cudldpHelloIntervalExt,_f:cudldpFastHelloLinkFailRptNotifEnable,_g:cudldpFastHelloStatusChangeNotifEnable,'cudldpInterface':cudldpInterface,'cudldpInterfaceTable':cudldpInterfaceTable,'cudldpInterfaceEntry':cudldpInterfaceEntry,_Y:cudldpInterfaceEnable,_N:cudldpInterfaceOperStatus,_Z:cudldpInterfaceAggressiveMode,_b:cudldpInterfaceAdminMode,_c:cudldpInterfaceOperMode,_O:cudldpIfFastHelloInterval,_P:cudldpIfOperHelloInterval,_Q:cudldpIfFastHelloOperStatus,'cudldpFastHello':cudldpFastHello,_e:cudldpFastHelloErrorReportEnable,_h:cudldpFastHelloMaxPorts,_i:cudldpFastHelloConfigPorts,_j:cudldpFastHelloOperationalPorts,'ciscoUdldpMIBConformance':ciscoUdldpMIBConformance,'ciscoUdldpMIBCompliances':ciscoUdldpMIBCompliances,'ciscoUdldpMIBCompliance':ciscoUdldpMIBCompliance,'ciscoUdldpMIBComplianceRev1':ciscoUdldpMIBComplianceRev1,'ciscoUdldpMIBComplianceRev2':ciscoUdldpMIBComplianceRev2,'ciscoUdldpMIBComplianceRev3':ciscoUdldpMIBComplianceRev3,'ciscoUdldpMIBComplianceRev4':ciscoUdldpMIBComplianceRev4,'ciscoUdldpMIBGroups':ciscoUdldpMIBGroups,_R:ciscoUdldpMIBGroup,_m:ciscoUdldpAggreModeOptionalGroup,_I:ciscoUdldpMIBGroup2,_S:ciscoUdldpMIBGroup3,_n:ciscoUdldpFastHelloGroup,_o:ciscoUdldpFastHelloNotificationGroup})