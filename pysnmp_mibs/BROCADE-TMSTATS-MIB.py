_M='bcsiTMVOQIngressStatsPriority'
_L='bcsiTMVOQIngressStatsEgressPort'
_K='bcsiTMVOQIngressStatsTower'
_J='bcsiTMVOQIngressStatsSlot'
_I='bcsiTMVOQCPUGroupStatsPriority'
_H='bcsiTMVOQCPUGroupStatsGroup'
_G='bcsiTMVOQCPUGroupStatsSlot'
_F='bcsiTMStatsTower'
_E='bcsiTMStatsSlot'
_D='not-accessible'
_C='BROCADE-TMSTATS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bcsiModules,=mibBuilder.importSymbols('Brocade-REG-MIB','bcsiModules')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bcsiTMStats=ModuleIdentity((1,3,6,1,4,1,1588,3,1,15))
if mibBuilder.loadTexts:bcsiTMStats.setRevisions(('2018-05-29 12:00','2016-10-21 13:30'))
_BcsiTMStatsNotification_ObjectIdentity=ObjectIdentity
bcsiTMStatsNotification=_BcsiTMStatsNotification_ObjectIdentity((1,3,6,1,4,1,1588,3,1,15,0))
_BcsiTMStatsObjects_ObjectIdentity=ObjectIdentity
bcsiTMStatsObjects=_BcsiTMStatsObjects_ObjectIdentity((1,3,6,1,4,1,1588,3,1,15,1))
_BcsiTMStatsGlobals_ObjectIdentity=ObjectIdentity
bcsiTMStatsGlobals=_BcsiTMStatsGlobals_ObjectIdentity((1,3,6,1,4,1,1588,3,1,15,1,1))
_BcsiTMStatsInfoGroup_ObjectIdentity=ObjectIdentity
bcsiTMStatsInfoGroup=_BcsiTMStatsInfoGroup_ObjectIdentity((1,3,6,1,4,1,1588,3,1,15,1,2))
_BcsiTMStatsInfoGroupGlobals_ObjectIdentity=ObjectIdentity
bcsiTMStatsInfoGroupGlobals=_BcsiTMStatsInfoGroupGlobals_ObjectIdentity((1,3,6,1,4,1,1588,3,1,15,1,2,1))
_BcsiTMStatsTable_Object=MibTable
bcsiTMStatsTable=_BcsiTMStatsTable_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2))
if mibBuilder.loadTexts:bcsiTMStatsTable.setStatus(_A)
_BcsiTMStatsEntry_Object=MibTableRow
bcsiTMStatsEntry=_BcsiTMStatsEntry_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1))
bcsiTMStatsEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:bcsiTMStatsEntry.setStatus(_A)
_BcsiTMStatsSlot_Type=Unsigned32
_BcsiTMStatsSlot_Object=MibTableColumn
bcsiTMStatsSlot=_BcsiTMStatsSlot_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,1),_BcsiTMStatsSlot_Type())
bcsiTMStatsSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:bcsiTMStatsSlot.setStatus(_A)
_BcsiTMStatsTower_Type=Unsigned32
_BcsiTMStatsTower_Object=MibTableColumn
bcsiTMStatsTower=_BcsiTMStatsTower_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,2),_BcsiTMStatsTower_Type())
bcsiTMStatsTower.setMaxAccess(_D)
if mibBuilder.loadTexts:bcsiTMStatsTower.setStatus(_A)
_BcsiTMStatsDescription_Type=DisplayString
_BcsiTMStatsDescription_Object=MibTableColumn
bcsiTMStatsDescription=_BcsiTMStatsDescription_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,3),_BcsiTMStatsDescription_Type())
bcsiTMStatsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsDescription.setStatus(_A)
_BcsiTMStatsTotalIngressPkts_Type=Counter64
_BcsiTMStatsTotalIngressPkts_Object=MibTableColumn
bcsiTMStatsTotalIngressPkts=_BcsiTMStatsTotalIngressPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,4),_BcsiTMStatsTotalIngressPkts_Type())
bcsiTMStatsTotalIngressPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsTotalIngressPkts.setStatus(_A)
_BcsiTMStatsIngressCPUPkts_Type=Counter64
_BcsiTMStatsIngressCPUPkts_Object=MibTableColumn
bcsiTMStatsIngressCPUPkts=_BcsiTMStatsIngressCPUPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,5),_BcsiTMStatsIngressCPUPkts_Type())
bcsiTMStatsIngressCPUPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsIngressCPUPkts.setStatus(_A)
_BcsiTMStatsIngressEnquePkts_Type=Counter64
_BcsiTMStatsIngressEnquePkts_Object=MibTableColumn
bcsiTMStatsIngressEnquePkts=_BcsiTMStatsIngressEnquePkts_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,6),_BcsiTMStatsIngressEnquePkts_Type())
bcsiTMStatsIngressEnquePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsIngressEnquePkts.setStatus(_A)
_BcsiTMStatsIngressDequePkts_Type=Counter64
_BcsiTMStatsIngressDequePkts_Object=MibTableColumn
bcsiTMStatsIngressDequePkts=_BcsiTMStatsIngressDequePkts_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,7),_BcsiTMStatsIngressDequePkts_Type())
bcsiTMStatsIngressDequePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsIngressDequePkts.setStatus(_A)
_BcsiTMStatsIngressTotalDiscardPkts_Type=Counter64
_BcsiTMStatsIngressTotalDiscardPkts_Object=MibTableColumn
bcsiTMStatsIngressTotalDiscardPkts=_BcsiTMStatsIngressTotalDiscardPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,8),_BcsiTMStatsIngressTotalDiscardPkts_Type())
bcsiTMStatsIngressTotalDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsIngressTotalDiscardPkts.setStatus(_A)
_BcsiTMStatsIngressOldestDiscardPkts_Type=Counter64
_BcsiTMStatsIngressOldestDiscardPkts_Object=MibTableColumn
bcsiTMStatsIngressOldestDiscardPkts=_BcsiTMStatsIngressOldestDiscardPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,9),_BcsiTMStatsIngressOldestDiscardPkts_Type())
bcsiTMStatsIngressOldestDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsIngressOldestDiscardPkts.setStatus(_A)
_BcsiTMStatsIngressResolvedToBeDropped_Type=Counter64
_BcsiTMStatsIngressResolvedToBeDropped_Object=MibTableColumn
bcsiTMStatsIngressResolvedToBeDropped=_BcsiTMStatsIngressResolvedToBeDropped_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,10),_BcsiTMStatsIngressResolvedToBeDropped_Type())
bcsiTMStatsIngressResolvedToBeDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsIngressResolvedToBeDropped.setStatus(_A)
_BcsiTMStatsIngressCRCErrorCount_Type=Counter64
_BcsiTMStatsIngressCRCErrorCount_Object=MibTableColumn
bcsiTMStatsIngressCRCErrorCount=_BcsiTMStatsIngressCRCErrorCount_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,11),_BcsiTMStatsIngressCRCErrorCount_Type())
bcsiTMStatsIngressCRCErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsIngressCRCErrorCount.setStatus(_A)
_BcsiTMStatsEgressREDiscardPkts_Type=Counter64
_BcsiTMStatsEgressREDiscardPkts_Object=MibTableColumn
bcsiTMStatsEgressREDiscardPkts=_BcsiTMStatsEgressREDiscardPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,12),_BcsiTMStatsEgressREDiscardPkts_Type())
bcsiTMStatsEgressREDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsEgressREDiscardPkts.setStatus(_A)
_BcsiTMStatsEgressFilterDiscardPkts_Type=Counter64
_BcsiTMStatsEgressFilterDiscardPkts_Object=MibTableColumn
bcsiTMStatsEgressFilterDiscardPkts=_BcsiTMStatsEgressFilterDiscardPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,13),_BcsiTMStatsEgressFilterDiscardPkts_Type())
bcsiTMStatsEgressFilterDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsEgressFilterDiscardPkts.setStatus(_A)
_BcsiTMStatsEgressDiscardUCPkts_Type=Counter64
_BcsiTMStatsEgressDiscardUCPkts_Object=MibTableColumn
bcsiTMStatsEgressDiscardUCPkts=_BcsiTMStatsEgressDiscardUCPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,14),_BcsiTMStatsEgressDiscardUCPkts_Type())
bcsiTMStatsEgressDiscardUCPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsEgressDiscardUCPkts.setStatus(_A)
_BcsiTMStatsEgressDiscardMCPkts_Type=Counter64
_BcsiTMStatsEgressDiscardMCPkts_Object=MibTableColumn
bcsiTMStatsEgressDiscardMCPkts=_BcsiTMStatsEgressDiscardMCPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,15),_BcsiTMStatsEgressDiscardMCPkts_Type())
bcsiTMStatsEgressDiscardMCPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsEgressDiscardMCPkts.setStatus(_A)
_BcsiTMStatsEgressUnicastPkts_Type=Counter64
_BcsiTMStatsEgressUnicastPkts_Object=MibTableColumn
bcsiTMStatsEgressUnicastPkts=_BcsiTMStatsEgressUnicastPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,16),_BcsiTMStatsEgressUnicastPkts_Type())
bcsiTMStatsEgressUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsEgressUnicastPkts.setStatus(_A)
_BcsiTMStatsEgressMulticastPkts_Type=Counter64
_BcsiTMStatsEgressMulticastPkts_Object=MibTableColumn
bcsiTMStatsEgressMulticastPkts=_BcsiTMStatsEgressMulticastPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,17),_BcsiTMStatsEgressMulticastPkts_Type())
bcsiTMStatsEgressMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsEgressMulticastPkts.setStatus(_A)
_BcsiTMStatsEgressFQPPkts_Type=Counter64
_BcsiTMStatsEgressFQPPkts_Object=MibTableColumn
bcsiTMStatsEgressFQPPkts=_BcsiTMStatsEgressFQPPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,2,2,1,18),_BcsiTMStatsEgressFQPPkts_Type())
bcsiTMStatsEgressFQPPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMStatsEgressFQPPkts.setStatus(_A)
_BcsiTMVOQStatsInfoGroup_ObjectIdentity=ObjectIdentity
bcsiTMVOQStatsInfoGroup=_BcsiTMVOQStatsInfoGroup_ObjectIdentity((1,3,6,1,4,1,1588,3,1,15,1,3))
_BcsiTMVOQStatsInfoGroupGlobals_ObjectIdentity=ObjectIdentity
bcsiTMVOQStatsInfoGroupGlobals=_BcsiTMVOQStatsInfoGroupGlobals_ObjectIdentity((1,3,6,1,4,1,1588,3,1,15,1,3,1))
_BcsiTMVOQCPUGroupStatsTable_Object=MibTable
bcsiTMVOQCPUGroupStatsTable=_BcsiTMVOQCPUGroupStatsTable_Object((1,3,6,1,4,1,1588,3,1,15,1,3,2))
if mibBuilder.loadTexts:bcsiTMVOQCPUGroupStatsTable.setStatus(_A)
_BcsiTMVOQCPUGroupStatsEntry_Object=MibTableRow
bcsiTMVOQCPUGroupStatsEntry=_BcsiTMVOQCPUGroupStatsEntry_Object((1,3,6,1,4,1,1588,3,1,15,1,3,2,1))
bcsiTMVOQCPUGroupStatsEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:bcsiTMVOQCPUGroupStatsEntry.setStatus(_A)
_BcsiTMVOQCPUGroupStatsSlot_Type=Unsigned32
_BcsiTMVOQCPUGroupStatsSlot_Object=MibTableColumn
bcsiTMVOQCPUGroupStatsSlot=_BcsiTMVOQCPUGroupStatsSlot_Object((1,3,6,1,4,1,1588,3,1,15,1,3,2,1,1),_BcsiTMVOQCPUGroupStatsSlot_Type())
bcsiTMVOQCPUGroupStatsSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:bcsiTMVOQCPUGroupStatsSlot.setStatus(_A)
_BcsiTMVOQCPUGroupStatsGroup_Type=Unsigned32
_BcsiTMVOQCPUGroupStatsGroup_Object=MibTableColumn
bcsiTMVOQCPUGroupStatsGroup=_BcsiTMVOQCPUGroupStatsGroup_Object((1,3,6,1,4,1,1588,3,1,15,1,3,2,1,2),_BcsiTMVOQCPUGroupStatsGroup_Type())
bcsiTMVOQCPUGroupStatsGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:bcsiTMVOQCPUGroupStatsGroup.setStatus(_A)
_BcsiTMVOQCPUGroupStatsPriority_Type=Unsigned32
_BcsiTMVOQCPUGroupStatsPriority_Object=MibTableColumn
bcsiTMVOQCPUGroupStatsPriority=_BcsiTMVOQCPUGroupStatsPriority_Object((1,3,6,1,4,1,1588,3,1,15,1,3,2,1,3),_BcsiTMVOQCPUGroupStatsPriority_Type())
bcsiTMVOQCPUGroupStatsPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:bcsiTMVOQCPUGroupStatsPriority.setStatus(_A)
_BcsiTMVOQCPUGroupStatsDescription_Type=DisplayString
_BcsiTMVOQCPUGroupStatsDescription_Object=MibTableColumn
bcsiTMVOQCPUGroupStatsDescription=_BcsiTMVOQCPUGroupStatsDescription_Object((1,3,6,1,4,1,1588,3,1,15,1,3,2,1,4),_BcsiTMVOQCPUGroupStatsDescription_Type())
bcsiTMVOQCPUGroupStatsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMVOQCPUGroupStatsDescription.setStatus(_A)
_BcsiTMVOQCPUGroupStatsEnQPkts_Type=Counter64
_BcsiTMVOQCPUGroupStatsEnQPkts_Object=MibTableColumn
bcsiTMVOQCPUGroupStatsEnQPkts=_BcsiTMVOQCPUGroupStatsEnQPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,3,2,1,5),_BcsiTMVOQCPUGroupStatsEnQPkts_Type())
bcsiTMVOQCPUGroupStatsEnQPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMVOQCPUGroupStatsEnQPkts.setStatus(_A)
_BcsiTMVOQCPUGroupStatsEnQBytes_Type=Counter64
_BcsiTMVOQCPUGroupStatsEnQBytes_Object=MibTableColumn
bcsiTMVOQCPUGroupStatsEnQBytes=_BcsiTMVOQCPUGroupStatsEnQBytes_Object((1,3,6,1,4,1,1588,3,1,15,1,3,2,1,6),_BcsiTMVOQCPUGroupStatsEnQBytes_Type())
bcsiTMVOQCPUGroupStatsEnQBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMVOQCPUGroupStatsEnQBytes.setStatus(_A)
_BcsiTMVOQCPUGroupStatsTotalDiscardPkts_Type=Counter64
_BcsiTMVOQCPUGroupStatsTotalDiscardPkts_Object=MibTableColumn
bcsiTMVOQCPUGroupStatsTotalDiscardPkts=_BcsiTMVOQCPUGroupStatsTotalDiscardPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,3,2,1,7),_BcsiTMVOQCPUGroupStatsTotalDiscardPkts_Type())
bcsiTMVOQCPUGroupStatsTotalDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMVOQCPUGroupStatsTotalDiscardPkts.setStatus(_A)
_BcsiTMVOQCPUGroupStatsTotalDiscardBytes_Type=Counter64
_BcsiTMVOQCPUGroupStatsTotalDiscardBytes_Object=MibTableColumn
bcsiTMVOQCPUGroupStatsTotalDiscardBytes=_BcsiTMVOQCPUGroupStatsTotalDiscardBytes_Object((1,3,6,1,4,1,1588,3,1,15,1,3,2,1,8),_BcsiTMVOQCPUGroupStatsTotalDiscardBytes_Type())
bcsiTMVOQCPUGroupStatsTotalDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMVOQCPUGroupStatsTotalDiscardBytes.setStatus(_A)
_BcsiTMVOQCPUGroupStatsCurrQDepth_Type=Counter64
_BcsiTMVOQCPUGroupStatsCurrQDepth_Object=MibTableColumn
bcsiTMVOQCPUGroupStatsCurrQDepth=_BcsiTMVOQCPUGroupStatsCurrQDepth_Object((1,3,6,1,4,1,1588,3,1,15,1,3,2,1,9),_BcsiTMVOQCPUGroupStatsCurrQDepth_Type())
bcsiTMVOQCPUGroupStatsCurrQDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMVOQCPUGroupStatsCurrQDepth.setStatus(_A)
_BcsiTMVOQCPUGroupStatsMaxQDepth_Type=Counter64
_BcsiTMVOQCPUGroupStatsMaxQDepth_Object=MibTableColumn
bcsiTMVOQCPUGroupStatsMaxQDepth=_BcsiTMVOQCPUGroupStatsMaxQDepth_Object((1,3,6,1,4,1,1588,3,1,15,1,3,2,1,10),_BcsiTMVOQCPUGroupStatsMaxQDepth_Type())
bcsiTMVOQCPUGroupStatsMaxQDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMVOQCPUGroupStatsMaxQDepth.setStatus(_A)
_BcsiTMVOQIngressStatsTable_Object=MibTable
bcsiTMVOQIngressStatsTable=_BcsiTMVOQIngressStatsTable_Object((1,3,6,1,4,1,1588,3,1,15,1,3,3))
if mibBuilder.loadTexts:bcsiTMVOQIngressStatsTable.setStatus(_A)
_BcsiTMVOQIngressStatsEntry_Object=MibTableRow
bcsiTMVOQIngressStatsEntry=_BcsiTMVOQIngressStatsEntry_Object((1,3,6,1,4,1,1588,3,1,15,1,3,3,1))
bcsiTMVOQIngressStatsEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:bcsiTMVOQIngressStatsEntry.setStatus(_A)
_BcsiTMVOQIngressStatsSlot_Type=Unsigned32
_BcsiTMVOQIngressStatsSlot_Object=MibTableColumn
bcsiTMVOQIngressStatsSlot=_BcsiTMVOQIngressStatsSlot_Object((1,3,6,1,4,1,1588,3,1,15,1,3,3,1,1),_BcsiTMVOQIngressStatsSlot_Type())
bcsiTMVOQIngressStatsSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:bcsiTMVOQIngressStatsSlot.setStatus(_A)
_BcsiTMVOQIngressStatsTower_Type=Unsigned32
_BcsiTMVOQIngressStatsTower_Object=MibTableColumn
bcsiTMVOQIngressStatsTower=_BcsiTMVOQIngressStatsTower_Object((1,3,6,1,4,1,1588,3,1,15,1,3,3,1,2),_BcsiTMVOQIngressStatsTower_Type())
bcsiTMVOQIngressStatsTower.setMaxAccess(_D)
if mibBuilder.loadTexts:bcsiTMVOQIngressStatsTower.setStatus(_A)
_BcsiTMVOQIngressStatsEgressPort_Type=InterfaceIndex
_BcsiTMVOQIngressStatsEgressPort_Object=MibTableColumn
bcsiTMVOQIngressStatsEgressPort=_BcsiTMVOQIngressStatsEgressPort_Object((1,3,6,1,4,1,1588,3,1,15,1,3,3,1,3),_BcsiTMVOQIngressStatsEgressPort_Type())
bcsiTMVOQIngressStatsEgressPort.setMaxAccess(_D)
if mibBuilder.loadTexts:bcsiTMVOQIngressStatsEgressPort.setStatus(_A)
_BcsiTMVOQIngressStatsPriority_Type=Unsigned32
_BcsiTMVOQIngressStatsPriority_Object=MibTableColumn
bcsiTMVOQIngressStatsPriority=_BcsiTMVOQIngressStatsPriority_Object((1,3,6,1,4,1,1588,3,1,15,1,3,3,1,4),_BcsiTMVOQIngressStatsPriority_Type())
bcsiTMVOQIngressStatsPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:bcsiTMVOQIngressStatsPriority.setStatus(_A)
_BcsiTMVOQIngressStatsDescription_Type=DisplayString
_BcsiTMVOQIngressStatsDescription_Object=MibTableColumn
bcsiTMVOQIngressStatsDescription=_BcsiTMVOQIngressStatsDescription_Object((1,3,6,1,4,1,1588,3,1,15,1,3,3,1,5),_BcsiTMVOQIngressStatsDescription_Type())
bcsiTMVOQIngressStatsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMVOQIngressStatsDescription.setStatus(_A)
_BcsiTMVOQIngressStatsEnQPkts_Type=Counter64
_BcsiTMVOQIngressStatsEnQPkts_Object=MibTableColumn
bcsiTMVOQIngressStatsEnQPkts=_BcsiTMVOQIngressStatsEnQPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,3,3,1,6),_BcsiTMVOQIngressStatsEnQPkts_Type())
bcsiTMVOQIngressStatsEnQPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMVOQIngressStatsEnQPkts.setStatus(_A)
_BcsiTMVOQIngressStatsEnQBytes_Type=Counter64
_BcsiTMVOQIngressStatsEnQBytes_Object=MibTableColumn
bcsiTMVOQIngressStatsEnQBytes=_BcsiTMVOQIngressStatsEnQBytes_Object((1,3,6,1,4,1,1588,3,1,15,1,3,3,1,7),_BcsiTMVOQIngressStatsEnQBytes_Type())
bcsiTMVOQIngressStatsEnQBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMVOQIngressStatsEnQBytes.setStatus(_A)
_BcsiTMVOQIngressStatsTotalDiscardPkts_Type=Counter64
_BcsiTMVOQIngressStatsTotalDiscardPkts_Object=MibTableColumn
bcsiTMVOQIngressStatsTotalDiscardPkts=_BcsiTMVOQIngressStatsTotalDiscardPkts_Object((1,3,6,1,4,1,1588,3,1,15,1,3,3,1,8),_BcsiTMVOQIngressStatsTotalDiscardPkts_Type())
bcsiTMVOQIngressStatsTotalDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMVOQIngressStatsTotalDiscardPkts.setStatus(_A)
_BcsiTMVOQIngressStatsTotalDiscardBytes_Type=Counter64
_BcsiTMVOQIngressStatsTotalDiscardBytes_Object=MibTableColumn
bcsiTMVOQIngressStatsTotalDiscardBytes=_BcsiTMVOQIngressStatsTotalDiscardBytes_Object((1,3,6,1,4,1,1588,3,1,15,1,3,3,1,9),_BcsiTMVOQIngressStatsTotalDiscardBytes_Type())
bcsiTMVOQIngressStatsTotalDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMVOQIngressStatsTotalDiscardBytes.setStatus(_A)
_BcsiTMVOQIngressStatsCurrQDepth_Type=Counter64
_BcsiTMVOQIngressStatsCurrQDepth_Object=MibTableColumn
bcsiTMVOQIngressStatsCurrQDepth=_BcsiTMVOQIngressStatsCurrQDepth_Object((1,3,6,1,4,1,1588,3,1,15,1,3,3,1,10),_BcsiTMVOQIngressStatsCurrQDepth_Type())
bcsiTMVOQIngressStatsCurrQDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMVOQIngressStatsCurrQDepth.setStatus(_A)
_BcsiTMVOQIngressStatsMaxQDepth_Type=Counter64
_BcsiTMVOQIngressStatsMaxQDepth_Object=MibTableColumn
bcsiTMVOQIngressStatsMaxQDepth=_BcsiTMVOQIngressStatsMaxQDepth_Object((1,3,6,1,4,1,1588,3,1,15,1,3,3,1,11),_BcsiTMVOQIngressStatsMaxQDepth_Type())
bcsiTMVOQIngressStatsMaxQDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTMVOQIngressStatsMaxQDepth.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'bcsiTMStats':bcsiTMStats,'bcsiTMStatsNotification':bcsiTMStatsNotification,'bcsiTMStatsObjects':bcsiTMStatsObjects,'bcsiTMStatsGlobals':bcsiTMStatsGlobals,'bcsiTMStatsInfoGroup':bcsiTMStatsInfoGroup,'bcsiTMStatsInfoGroupGlobals':bcsiTMStatsInfoGroupGlobals,'bcsiTMStatsTable':bcsiTMStatsTable,'bcsiTMStatsEntry':bcsiTMStatsEntry,_E:bcsiTMStatsSlot,_F:bcsiTMStatsTower,'bcsiTMStatsDescription':bcsiTMStatsDescription,'bcsiTMStatsTotalIngressPkts':bcsiTMStatsTotalIngressPkts,'bcsiTMStatsIngressCPUPkts':bcsiTMStatsIngressCPUPkts,'bcsiTMStatsIngressEnquePkts':bcsiTMStatsIngressEnquePkts,'bcsiTMStatsIngressDequePkts':bcsiTMStatsIngressDequePkts,'bcsiTMStatsIngressTotalDiscardPkts':bcsiTMStatsIngressTotalDiscardPkts,'bcsiTMStatsIngressOldestDiscardPkts':bcsiTMStatsIngressOldestDiscardPkts,'bcsiTMStatsIngressResolvedToBeDropped':bcsiTMStatsIngressResolvedToBeDropped,'bcsiTMStatsIngressCRCErrorCount':bcsiTMStatsIngressCRCErrorCount,'bcsiTMStatsEgressREDiscardPkts':bcsiTMStatsEgressREDiscardPkts,'bcsiTMStatsEgressFilterDiscardPkts':bcsiTMStatsEgressFilterDiscardPkts,'bcsiTMStatsEgressDiscardUCPkts':bcsiTMStatsEgressDiscardUCPkts,'bcsiTMStatsEgressDiscardMCPkts':bcsiTMStatsEgressDiscardMCPkts,'bcsiTMStatsEgressUnicastPkts':bcsiTMStatsEgressUnicastPkts,'bcsiTMStatsEgressMulticastPkts':bcsiTMStatsEgressMulticastPkts,'bcsiTMStatsEgressFQPPkts':bcsiTMStatsEgressFQPPkts,'bcsiTMVOQStatsInfoGroup':bcsiTMVOQStatsInfoGroup,'bcsiTMVOQStatsInfoGroupGlobals':bcsiTMVOQStatsInfoGroupGlobals,'bcsiTMVOQCPUGroupStatsTable':bcsiTMVOQCPUGroupStatsTable,'bcsiTMVOQCPUGroupStatsEntry':bcsiTMVOQCPUGroupStatsEntry,_G:bcsiTMVOQCPUGroupStatsSlot,_H:bcsiTMVOQCPUGroupStatsGroup,_I:bcsiTMVOQCPUGroupStatsPriority,'bcsiTMVOQCPUGroupStatsDescription':bcsiTMVOQCPUGroupStatsDescription,'bcsiTMVOQCPUGroupStatsEnQPkts':bcsiTMVOQCPUGroupStatsEnQPkts,'bcsiTMVOQCPUGroupStatsEnQBytes':bcsiTMVOQCPUGroupStatsEnQBytes,'bcsiTMVOQCPUGroupStatsTotalDiscardPkts':bcsiTMVOQCPUGroupStatsTotalDiscardPkts,'bcsiTMVOQCPUGroupStatsTotalDiscardBytes':bcsiTMVOQCPUGroupStatsTotalDiscardBytes,'bcsiTMVOQCPUGroupStatsCurrQDepth':bcsiTMVOQCPUGroupStatsCurrQDepth,'bcsiTMVOQCPUGroupStatsMaxQDepth':bcsiTMVOQCPUGroupStatsMaxQDepth,'bcsiTMVOQIngressStatsTable':bcsiTMVOQIngressStatsTable,'bcsiTMVOQIngressStatsEntry':bcsiTMVOQIngressStatsEntry,_J:bcsiTMVOQIngressStatsSlot,_K:bcsiTMVOQIngressStatsTower,_L:bcsiTMVOQIngressStatsEgressPort,_M:bcsiTMVOQIngressStatsPriority,'bcsiTMVOQIngressStatsDescription':bcsiTMVOQIngressStatsDescription,'bcsiTMVOQIngressStatsEnQPkts':bcsiTMVOQIngressStatsEnQPkts,'bcsiTMVOQIngressStatsEnQBytes':bcsiTMVOQIngressStatsEnQBytes,'bcsiTMVOQIngressStatsTotalDiscardPkts':bcsiTMVOQIngressStatsTotalDiscardPkts,'bcsiTMVOQIngressStatsTotalDiscardBytes':bcsiTMVOQIngressStatsTotalDiscardBytes,'bcsiTMVOQIngressStatsCurrQDepth':bcsiTMVOQIngressStatsCurrQDepth,'bcsiTMVOQIngressStatsMaxQDepth':bcsiTMVOQIngressStatsMaxQDepth})