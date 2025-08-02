_AZ='etsysPimExtTibMgrGroup'
_AY='etsysPimExtNbrMgrGroup'
_AX='etsysPimExtIfStatsGroup'
_AW='etsysPimExtNbrStatsGroup'
_AV='etsysPimExtGroupMappingGroup'
_AU='etsysPimExtAnycastRPSetGroup'
_AT='etsysPimExtStaticRPGroup'
_AS='etsysPimExtIfGroup'
_AR='etsysPimExtTibMgrKeepalivePeriod'
_AQ='etsysPimExtTibMgrRegProbeTime'
_AP='etsysPimExtTibMgrRegSuppressionTime'
_AO='etsysPimExtTibMgrSGIStateStored'
_AN='etsysPimExtTibMgrSGIStateWarnThold'
_AM='etsysPimExtTibMgrSGIStateLimit'
_AL='etsysPimExtTibMgrStarGIStateStored'
_AK='etsysPimExtTibMgrStarGIStateWarnThold'
_AJ='etsysPimExtTibMgrStarGIStateLimit'
_AI='etsysPimExtTibMgrSGStateStored'
_AH='etsysPimExtTibMgrSGStateWarnThold'
_AG='etsysPimExtTibMgrSGStateLimit'
_AF='etsysPimExtTibMgrGStateStored'
_AE='etsysPimExtTibMgrGStateWarnThold'
_AD='etsysPimExtTibMgrGStateLimit'
_AC='etsysPimExtNbrMgrNumRecvBadLength'
_AB='etsysPimExtNbrMgrNumRecvBadChecksum'
_AA='etsysPimExtNbrMgrNumRecvUnknownVer'
_A9='etsysPimExtNbrMgrNumRecvUnknownType'
_A8='etsysPimExtNbrMgrNumRecvIgnoredType'
_A7='etsysPimExtNbrMgrNumErrRegisterStop'
_A6='etsysPimExtNbrMgrNumErrRegister'
_A5='etsysPimExtNbrMgrNumErrCRPAdvert'
_A4='etsysPimExtNbrMgrNumRecvRegisterStop'
_A3='etsysPimExtNbrMgrNumRecvRegister'
_A2='etsysPimExtNbrMgrNumRecvCRPAdvert'
_A1='etsysPimExtNbrMgrNumSentRegisterStop'
_A0='etsysPimExtNbrMgrNumSentRegister'
_z='etsysPimExtNbrMgrNumSentCRPAdvert'
_y='etsysPimExtNbrMgrAcceptUnicastBsms'
_x='etsysPimExtNbrMgrEnableUnicastMessages'
_w='etsysPimExtIfStatsNumUnknownHelloOpt'
_v='etsysPimExtIfStatsNumRecvUnknownNbr'
_u='etsysPimExtIfStatsNumErrHello'
_t='etsysPimExtIfStatsNumSentBsm'
_s='etsysPimExtIfStatsNumSentAssert'
_r='etsysPimExtIfStatsNumSentJoinPrune'
_q='etsysPimExtIfStatsNumSentHello'
_p='etsysPimExtNbrStatsNumErrBSM'
_o='etsysPimExtNbrStatsNumErrAssert'
_n='etsysPimExtNbrStatsNumErrJoinPrune'
_m='etsysPimExtNbrStatsNumRecvBSM'
_l='etsysPimExtNbrStatsNumRecvAssert'
_k='etsysPimExtNbrStatsNumRecvJoinPrune'
_j='etsysPimExtNbrStatsNumRecvHello'
_i='etsysPimExtGroupMappingIsInactive'
_h='etsysPimExtAnycastRPSetAdminStatus'
_g='etsysPimExtStaticRPAdminStatus'
_f='etsysPimExtIfAssertHoldtime'
_e='etsysPimExtIfAssertInterval'
_d='etsysPimExtIfSGStateStored'
_c='etsysPimExtIfSGStateWarnThold'
_b='etsysPimExtIfSGStateLimit'
_a='etsysPimExtIfStarGStateStored'
_Z='etsysPimExtIfStarGStateWarnThold'
_Y='etsysPimExtIfStarGStateLimit'
_X='etsysPimExtIfNeighborCount'
_W='etsysPimExtIfP2PNoHellos'
_V='etsysPimExtIfOperStatus'
_U='etsysPimExtIfAdminStatus'
_T='etsysPimExtIfStatsEntry'
_S='etsysPimExtNbrStatsEntry'
_R='etsysPimExtGroupMappingEntry'
_Q='etsysPimExtAnycastRPSetEntry'
_P='etsysPimExtStaticRPEntry'
_O='etsysPimExtIfEntry'
_N='not-accessible'
_M='etsysPimExtTibMgrIndex'
_L='etsysPimExtNbrMgrIndex'
_K='adminStatusDown'
_J='adminStatusUp'
_I='TruthValue'
_H='seconds'
_G='Integer32'
_F='read-create'
_E='read-write'
_D='Unsigned32'
_C='read-only'
_B='ENTERASYS-PIM-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InetVersion,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetVersion')
pimAnycastRPSetEntry,pimGroupMappingEntry,pimInterfaceEntry,pimNeighborEntry,pimStaticRPEntry=mibBuilder.importSymbols('PIM-STD-MIB','pimAnycastRPSetEntry','pimGroupMappingEntry','pimInterfaceEntry','pimNeighborEntry','pimStaticRPEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I)
etsysPimExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,67))
if mibBuilder.loadTexts:etsysPimExtMIB.setRevisions(('2009-02-24 22:32',))
_EtsysPimExtObjects_ObjectIdentity=ObjectIdentity
etsysPimExtObjects=_EtsysPimExtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,67,1))
_EtsysPimExtGlobals_ObjectIdentity=ObjectIdentity
etsysPimExtGlobals=_EtsysPimExtGlobals_ObjectIdentity((1,3,6,1,4,1,5624,1,2,67,1,1))
_EtsysPimExtTables_ObjectIdentity=ObjectIdentity
etsysPimExtTables=_EtsysPimExtTables_ObjectIdentity((1,3,6,1,4,1,5624,1,2,67,1,2))
_EtsysPimExtIfTable_Object=MibTable
etsysPimExtIfTable=_EtsysPimExtIfTable_Object((1,3,6,1,4,1,5624,1,2,67,1,2,1))
if mibBuilder.loadTexts:etsysPimExtIfTable.setStatus(_A)
_EtsysPimExtIfEntry_Object=MibTableRow
etsysPimExtIfEntry=_EtsysPimExtIfEntry_Object((1,3,6,1,4,1,5624,1,2,67,1,2,1,1))
if mibBuilder.loadTexts:etsysPimExtIfEntry.setStatus(_A)
class _EtsysPimExtIfAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_EtsysPimExtIfAdminStatus_Type.__name__=_G
_EtsysPimExtIfAdminStatus_Object=MibTableColumn
etsysPimExtIfAdminStatus=_EtsysPimExtIfAdminStatus_Object((1,3,6,1,4,1,5624,1,2,67,1,2,1,1,1),_EtsysPimExtIfAdminStatus_Type())
etsysPimExtIfAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysPimExtIfAdminStatus.setStatus(_A)
class _EtsysPimExtIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,8,10,11)));namedValues=NamedValues(*(('operStatusUp',1),('operStatusDown',2),('operStatusGoingUp',3),('operStatusGoingDown',4),('operStatusActFailed',5),('operStatusFailed',8),('operStatusFailedPerm',10),('operStatusFailing',11)))
_EtsysPimExtIfOperStatus_Type.__name__=_G
_EtsysPimExtIfOperStatus_Object=MibTableColumn
etsysPimExtIfOperStatus=_EtsysPimExtIfOperStatus_Object((1,3,6,1,4,1,5624,1,2,67,1,2,1,1,2),_EtsysPimExtIfOperStatus_Type())
etsysPimExtIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtIfOperStatus.setStatus(_A)
class _EtsysPimExtIfP2PNoHellos_Type(TruthValue):defaultValue=2
_EtsysPimExtIfP2PNoHellos_Type.__name__=_I
_EtsysPimExtIfP2PNoHellos_Object=MibTableColumn
etsysPimExtIfP2PNoHellos=_EtsysPimExtIfP2PNoHellos_Object((1,3,6,1,4,1,5624,1,2,67,1,2,1,1,3),_EtsysPimExtIfP2PNoHellos_Type())
etsysPimExtIfP2PNoHellos.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysPimExtIfP2PNoHellos.setStatus(_A)
_EtsysPimExtIfNeighborCount_Type=Gauge32
_EtsysPimExtIfNeighborCount_Object=MibTableColumn
etsysPimExtIfNeighborCount=_EtsysPimExtIfNeighborCount_Object((1,3,6,1,4,1,5624,1,2,67,1,2,1,1,4),_EtsysPimExtIfNeighborCount_Type())
etsysPimExtIfNeighborCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtIfNeighborCount.setStatus(_A)
class _EtsysPimExtIfStarGStateLimit_Type(Unsigned32):defaultValue=0
_EtsysPimExtIfStarGStateLimit_Type.__name__=_D
_EtsysPimExtIfStarGStateLimit_Object=MibTableColumn
etsysPimExtIfStarGStateLimit=_EtsysPimExtIfStarGStateLimit_Object((1,3,6,1,4,1,5624,1,2,67,1,2,1,1,5),_EtsysPimExtIfStarGStateLimit_Type())
etsysPimExtIfStarGStateLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysPimExtIfStarGStateLimit.setStatus(_A)
class _EtsysPimExtIfStarGStateWarnThold_Type(Unsigned32):defaultValue=0
_EtsysPimExtIfStarGStateWarnThold_Type.__name__=_D
_EtsysPimExtIfStarGStateWarnThold_Object=MibTableColumn
etsysPimExtIfStarGStateWarnThold=_EtsysPimExtIfStarGStateWarnThold_Object((1,3,6,1,4,1,5624,1,2,67,1,2,1,1,6),_EtsysPimExtIfStarGStateWarnThold_Type())
etsysPimExtIfStarGStateWarnThold.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysPimExtIfStarGStateWarnThold.setStatus(_A)
_EtsysPimExtIfStarGStateStored_Type=Gauge32
_EtsysPimExtIfStarGStateStored_Object=MibTableColumn
etsysPimExtIfStarGStateStored=_EtsysPimExtIfStarGStateStored_Object((1,3,6,1,4,1,5624,1,2,67,1,2,1,1,7),_EtsysPimExtIfStarGStateStored_Type())
etsysPimExtIfStarGStateStored.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtIfStarGStateStored.setStatus(_A)
class _EtsysPimExtIfSGStateLimit_Type(Unsigned32):defaultValue=0
_EtsysPimExtIfSGStateLimit_Type.__name__=_D
_EtsysPimExtIfSGStateLimit_Object=MibTableColumn
etsysPimExtIfSGStateLimit=_EtsysPimExtIfSGStateLimit_Object((1,3,6,1,4,1,5624,1,2,67,1,2,1,1,8),_EtsysPimExtIfSGStateLimit_Type())
etsysPimExtIfSGStateLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysPimExtIfSGStateLimit.setStatus(_A)
class _EtsysPimExtIfSGStateWarnThold_Type(Unsigned32):defaultValue=0
_EtsysPimExtIfSGStateWarnThold_Type.__name__=_D
_EtsysPimExtIfSGStateWarnThold_Object=MibTableColumn
etsysPimExtIfSGStateWarnThold=_EtsysPimExtIfSGStateWarnThold_Object((1,3,6,1,4,1,5624,1,2,67,1,2,1,1,9),_EtsysPimExtIfSGStateWarnThold_Type())
etsysPimExtIfSGStateWarnThold.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysPimExtIfSGStateWarnThold.setStatus(_A)
_EtsysPimExtIfSGStateStored_Type=Gauge32
_EtsysPimExtIfSGStateStored_Object=MibTableColumn
etsysPimExtIfSGStateStored=_EtsysPimExtIfSGStateStored_Object((1,3,6,1,4,1,5624,1,2,67,1,2,1,1,10),_EtsysPimExtIfSGStateStored_Type())
etsysPimExtIfSGStateStored.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtIfSGStateStored.setStatus(_A)
class _EtsysPimExtIfAssertInterval_Type(Unsigned32):defaultValue=177;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EtsysPimExtIfAssertInterval_Type.__name__=_D
_EtsysPimExtIfAssertInterval_Object=MibTableColumn
etsysPimExtIfAssertInterval=_EtsysPimExtIfAssertInterval_Object((1,3,6,1,4,1,5624,1,2,67,1,2,1,1,11),_EtsysPimExtIfAssertInterval_Type())
etsysPimExtIfAssertInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysPimExtIfAssertInterval.setStatus(_A)
if mibBuilder.loadTexts:etsysPimExtIfAssertInterval.setUnits(_H)
class _EtsysPimExtIfAssertHoldtime_Type(Unsigned32):defaultValue=180;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EtsysPimExtIfAssertHoldtime_Type.__name__=_D
_EtsysPimExtIfAssertHoldtime_Object=MibTableColumn
etsysPimExtIfAssertHoldtime=_EtsysPimExtIfAssertHoldtime_Object((1,3,6,1,4,1,5624,1,2,67,1,2,1,1,12),_EtsysPimExtIfAssertHoldtime_Type())
etsysPimExtIfAssertHoldtime.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysPimExtIfAssertHoldtime.setStatus(_A)
if mibBuilder.loadTexts:etsysPimExtIfAssertHoldtime.setUnits(_H)
_EtsysPimExtStaticRPTable_Object=MibTable
etsysPimExtStaticRPTable=_EtsysPimExtStaticRPTable_Object((1,3,6,1,4,1,5624,1,2,67,1,2,2))
if mibBuilder.loadTexts:etsysPimExtStaticRPTable.setStatus(_A)
_EtsysPimExtStaticRPEntry_Object=MibTableRow
etsysPimExtStaticRPEntry=_EtsysPimExtStaticRPEntry_Object((1,3,6,1,4,1,5624,1,2,67,1,2,2,1))
if mibBuilder.loadTexts:etsysPimExtStaticRPEntry.setStatus(_A)
class _EtsysPimExtStaticRPAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_EtsysPimExtStaticRPAdminStatus_Type.__name__=_G
_EtsysPimExtStaticRPAdminStatus_Object=MibTableColumn
etsysPimExtStaticRPAdminStatus=_EtsysPimExtStaticRPAdminStatus_Object((1,3,6,1,4,1,5624,1,2,67,1,2,2,1,1),_EtsysPimExtStaticRPAdminStatus_Type())
etsysPimExtStaticRPAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysPimExtStaticRPAdminStatus.setStatus(_A)
_EtsysPimExtAnycastRPSetTable_Object=MibTable
etsysPimExtAnycastRPSetTable=_EtsysPimExtAnycastRPSetTable_Object((1,3,6,1,4,1,5624,1,2,67,1,2,3))
if mibBuilder.loadTexts:etsysPimExtAnycastRPSetTable.setStatus(_A)
_EtsysPimExtAnycastRPSetEntry_Object=MibTableRow
etsysPimExtAnycastRPSetEntry=_EtsysPimExtAnycastRPSetEntry_Object((1,3,6,1,4,1,5624,1,2,67,1,2,3,1))
if mibBuilder.loadTexts:etsysPimExtAnycastRPSetEntry.setStatus(_A)
class _EtsysPimExtAnycastRPSetAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_EtsysPimExtAnycastRPSetAdminStatus_Type.__name__=_G
_EtsysPimExtAnycastRPSetAdminStatus_Object=MibTableColumn
etsysPimExtAnycastRPSetAdminStatus=_EtsysPimExtAnycastRPSetAdminStatus_Object((1,3,6,1,4,1,5624,1,2,67,1,2,3,1,1),_EtsysPimExtAnycastRPSetAdminStatus_Type())
etsysPimExtAnycastRPSetAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysPimExtAnycastRPSetAdminStatus.setStatus(_A)
_EtsysPimExtGroupMappingTable_Object=MibTable
etsysPimExtGroupMappingTable=_EtsysPimExtGroupMappingTable_Object((1,3,6,1,4,1,5624,1,2,67,1,2,4))
if mibBuilder.loadTexts:etsysPimExtGroupMappingTable.setStatus(_A)
_EtsysPimExtGroupMappingEntry_Object=MibTableRow
etsysPimExtGroupMappingEntry=_EtsysPimExtGroupMappingEntry_Object((1,3,6,1,4,1,5624,1,2,67,1,2,4,1))
if mibBuilder.loadTexts:etsysPimExtGroupMappingEntry.setStatus(_A)
_EtsysPimExtGroupMappingIsInactive_Type=TruthValue
_EtsysPimExtGroupMappingIsInactive_Object=MibTableColumn
etsysPimExtGroupMappingIsInactive=_EtsysPimExtGroupMappingIsInactive_Object((1,3,6,1,4,1,5624,1,2,67,1,2,4,1,1),_EtsysPimExtGroupMappingIsInactive_Type())
etsysPimExtGroupMappingIsInactive.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtGroupMappingIsInactive.setStatus(_A)
_EtsysPimExtNbrStatsTable_Object=MibTable
etsysPimExtNbrStatsTable=_EtsysPimExtNbrStatsTable_Object((1,3,6,1,4,1,5624,1,2,67,1,2,5))
if mibBuilder.loadTexts:etsysPimExtNbrStatsTable.setStatus(_A)
_EtsysPimExtNbrStatsEntry_Object=MibTableRow
etsysPimExtNbrStatsEntry=_EtsysPimExtNbrStatsEntry_Object((1,3,6,1,4,1,5624,1,2,67,1,2,5,1))
if mibBuilder.loadTexts:etsysPimExtNbrStatsEntry.setStatus(_A)
_EtsysPimExtNbrStatsNumRecvHello_Type=Counter32
_EtsysPimExtNbrStatsNumRecvHello_Object=MibTableColumn
etsysPimExtNbrStatsNumRecvHello=_EtsysPimExtNbrStatsNumRecvHello_Object((1,3,6,1,4,1,5624,1,2,67,1,2,5,1,1),_EtsysPimExtNbrStatsNumRecvHello_Type())
etsysPimExtNbrStatsNumRecvHello.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrStatsNumRecvHello.setStatus(_A)
_EtsysPimExtNbrStatsNumRecvJoinPrune_Type=Counter32
_EtsysPimExtNbrStatsNumRecvJoinPrune_Object=MibTableColumn
etsysPimExtNbrStatsNumRecvJoinPrune=_EtsysPimExtNbrStatsNumRecvJoinPrune_Object((1,3,6,1,4,1,5624,1,2,67,1,2,5,1,2),_EtsysPimExtNbrStatsNumRecvJoinPrune_Type())
etsysPimExtNbrStatsNumRecvJoinPrune.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrStatsNumRecvJoinPrune.setStatus(_A)
_EtsysPimExtNbrStatsNumRecvAssert_Type=Counter32
_EtsysPimExtNbrStatsNumRecvAssert_Object=MibTableColumn
etsysPimExtNbrStatsNumRecvAssert=_EtsysPimExtNbrStatsNumRecvAssert_Object((1,3,6,1,4,1,5624,1,2,67,1,2,5,1,3),_EtsysPimExtNbrStatsNumRecvAssert_Type())
etsysPimExtNbrStatsNumRecvAssert.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrStatsNumRecvAssert.setStatus(_A)
_EtsysPimExtNbrStatsNumRecvBSM_Type=Counter32
_EtsysPimExtNbrStatsNumRecvBSM_Object=MibTableColumn
etsysPimExtNbrStatsNumRecvBSM=_EtsysPimExtNbrStatsNumRecvBSM_Object((1,3,6,1,4,1,5624,1,2,67,1,2,5,1,4),_EtsysPimExtNbrStatsNumRecvBSM_Type())
etsysPimExtNbrStatsNumRecvBSM.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrStatsNumRecvBSM.setStatus(_A)
_EtsysPimExtNbrStatsNumErrJoinPrune_Type=Counter32
_EtsysPimExtNbrStatsNumErrJoinPrune_Object=MibTableColumn
etsysPimExtNbrStatsNumErrJoinPrune=_EtsysPimExtNbrStatsNumErrJoinPrune_Object((1,3,6,1,4,1,5624,1,2,67,1,2,5,1,5),_EtsysPimExtNbrStatsNumErrJoinPrune_Type())
etsysPimExtNbrStatsNumErrJoinPrune.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrStatsNumErrJoinPrune.setStatus(_A)
_EtsysPimExtNbrStatsNumErrAssert_Type=Counter32
_EtsysPimExtNbrStatsNumErrAssert_Object=MibTableColumn
etsysPimExtNbrStatsNumErrAssert=_EtsysPimExtNbrStatsNumErrAssert_Object((1,3,6,1,4,1,5624,1,2,67,1,2,5,1,6),_EtsysPimExtNbrStatsNumErrAssert_Type())
etsysPimExtNbrStatsNumErrAssert.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrStatsNumErrAssert.setStatus(_A)
_EtsysPimExtNbrStatsNumErrBSM_Type=Counter32
_EtsysPimExtNbrStatsNumErrBSM_Object=MibTableColumn
etsysPimExtNbrStatsNumErrBSM=_EtsysPimExtNbrStatsNumErrBSM_Object((1,3,6,1,4,1,5624,1,2,67,1,2,5,1,7),_EtsysPimExtNbrStatsNumErrBSM_Type())
etsysPimExtNbrStatsNumErrBSM.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrStatsNumErrBSM.setStatus(_A)
_EtsysPimExtIfStatsTable_Object=MibTable
etsysPimExtIfStatsTable=_EtsysPimExtIfStatsTable_Object((1,3,6,1,4,1,5624,1,2,67,1,2,6))
if mibBuilder.loadTexts:etsysPimExtIfStatsTable.setStatus(_A)
_EtsysPimExtIfStatsEntry_Object=MibTableRow
etsysPimExtIfStatsEntry=_EtsysPimExtIfStatsEntry_Object((1,3,6,1,4,1,5624,1,2,67,1,2,6,1))
if mibBuilder.loadTexts:etsysPimExtIfStatsEntry.setStatus(_A)
_EtsysPimExtIfStatsNumSentHello_Type=Counter32
_EtsysPimExtIfStatsNumSentHello_Object=MibTableColumn
etsysPimExtIfStatsNumSentHello=_EtsysPimExtIfStatsNumSentHello_Object((1,3,6,1,4,1,5624,1,2,67,1,2,6,1,1),_EtsysPimExtIfStatsNumSentHello_Type())
etsysPimExtIfStatsNumSentHello.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtIfStatsNumSentHello.setStatus(_A)
_EtsysPimExtIfStatsNumSentJoinPrune_Type=Counter32
_EtsysPimExtIfStatsNumSentJoinPrune_Object=MibTableColumn
etsysPimExtIfStatsNumSentJoinPrune=_EtsysPimExtIfStatsNumSentJoinPrune_Object((1,3,6,1,4,1,5624,1,2,67,1,2,6,1,2),_EtsysPimExtIfStatsNumSentJoinPrune_Type())
etsysPimExtIfStatsNumSentJoinPrune.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtIfStatsNumSentJoinPrune.setStatus(_A)
_EtsysPimExtIfStatsNumSentAssert_Type=Counter32
_EtsysPimExtIfStatsNumSentAssert_Object=MibTableColumn
etsysPimExtIfStatsNumSentAssert=_EtsysPimExtIfStatsNumSentAssert_Object((1,3,6,1,4,1,5624,1,2,67,1,2,6,1,3),_EtsysPimExtIfStatsNumSentAssert_Type())
etsysPimExtIfStatsNumSentAssert.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtIfStatsNumSentAssert.setStatus(_A)
_EtsysPimExtIfStatsNumSentBsm_Type=Counter32
_EtsysPimExtIfStatsNumSentBsm_Object=MibTableColumn
etsysPimExtIfStatsNumSentBsm=_EtsysPimExtIfStatsNumSentBsm_Object((1,3,6,1,4,1,5624,1,2,67,1,2,6,1,4),_EtsysPimExtIfStatsNumSentBsm_Type())
etsysPimExtIfStatsNumSentBsm.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtIfStatsNumSentBsm.setStatus(_A)
_EtsysPimExtIfStatsNumErrHello_Type=Counter32
_EtsysPimExtIfStatsNumErrHello_Object=MibTableColumn
etsysPimExtIfStatsNumErrHello=_EtsysPimExtIfStatsNumErrHello_Object((1,3,6,1,4,1,5624,1,2,67,1,2,6,1,5),_EtsysPimExtIfStatsNumErrHello_Type())
etsysPimExtIfStatsNumErrHello.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtIfStatsNumErrHello.setStatus(_A)
_EtsysPimExtIfStatsNumRecvUnknownNbr_Type=Counter32
_EtsysPimExtIfStatsNumRecvUnknownNbr_Object=MibTableColumn
etsysPimExtIfStatsNumRecvUnknownNbr=_EtsysPimExtIfStatsNumRecvUnknownNbr_Object((1,3,6,1,4,1,5624,1,2,67,1,2,6,1,6),_EtsysPimExtIfStatsNumRecvUnknownNbr_Type())
etsysPimExtIfStatsNumRecvUnknownNbr.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtIfStatsNumRecvUnknownNbr.setStatus(_A)
_EtsysPimExtIfStatsNumUnknownHelloOpt_Type=Counter32
_EtsysPimExtIfStatsNumUnknownHelloOpt_Object=MibTableColumn
etsysPimExtIfStatsNumUnknownHelloOpt=_EtsysPimExtIfStatsNumUnknownHelloOpt_Object((1,3,6,1,4,1,5624,1,2,67,1,2,6,1,7),_EtsysPimExtIfStatsNumUnknownHelloOpt_Type())
etsysPimExtIfStatsNumUnknownHelloOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtIfStatsNumUnknownHelloOpt.setStatus(_A)
_EtsysPimExtNbrMgrTable_Object=MibTable
etsysPimExtNbrMgrTable=_EtsysPimExtNbrMgrTable_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7))
if mibBuilder.loadTexts:etsysPimExtNbrMgrTable.setStatus(_A)
_EtsysPimExtNbrMgrEntry_Object=MibTableRow
etsysPimExtNbrMgrEntry=_EtsysPimExtNbrMgrEntry_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1))
etsysPimExtNbrMgrEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:etsysPimExtNbrMgrEntry.setStatus(_A)
_EtsysPimExtNbrMgrIndex_Type=InetVersion
_EtsysPimExtNbrMgrIndex_Object=MibTableColumn
etsysPimExtNbrMgrIndex=_EtsysPimExtNbrMgrIndex_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,1),_EtsysPimExtNbrMgrIndex_Type())
etsysPimExtNbrMgrIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:etsysPimExtNbrMgrIndex.setStatus(_A)
class _EtsysPimExtNbrMgrEnableUnicastMessages_Type(TruthValue):defaultValue=1
_EtsysPimExtNbrMgrEnableUnicastMessages_Type.__name__=_I
_EtsysPimExtNbrMgrEnableUnicastMessages_Object=MibTableColumn
etsysPimExtNbrMgrEnableUnicastMessages=_EtsysPimExtNbrMgrEnableUnicastMessages_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,2),_EtsysPimExtNbrMgrEnableUnicastMessages_Type())
etsysPimExtNbrMgrEnableUnicastMessages.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPimExtNbrMgrEnableUnicastMessages.setStatus(_A)
class _EtsysPimExtNbrMgrAcceptUnicastBsms_Type(TruthValue):defaultValue=2
_EtsysPimExtNbrMgrAcceptUnicastBsms_Type.__name__=_I
_EtsysPimExtNbrMgrAcceptUnicastBsms_Object=MibTableColumn
etsysPimExtNbrMgrAcceptUnicastBsms=_EtsysPimExtNbrMgrAcceptUnicastBsms_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,3),_EtsysPimExtNbrMgrAcceptUnicastBsms_Type())
etsysPimExtNbrMgrAcceptUnicastBsms.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPimExtNbrMgrAcceptUnicastBsms.setStatus(_A)
_EtsysPimExtNbrMgrNumSentCRPAdvert_Type=Counter32
_EtsysPimExtNbrMgrNumSentCRPAdvert_Object=MibTableColumn
etsysPimExtNbrMgrNumSentCRPAdvert=_EtsysPimExtNbrMgrNumSentCRPAdvert_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,4),_EtsysPimExtNbrMgrNumSentCRPAdvert_Type())
etsysPimExtNbrMgrNumSentCRPAdvert.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrMgrNumSentCRPAdvert.setStatus(_A)
_EtsysPimExtNbrMgrNumSentRegister_Type=Counter32
_EtsysPimExtNbrMgrNumSentRegister_Object=MibTableColumn
etsysPimExtNbrMgrNumSentRegister=_EtsysPimExtNbrMgrNumSentRegister_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,5),_EtsysPimExtNbrMgrNumSentRegister_Type())
etsysPimExtNbrMgrNumSentRegister.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrMgrNumSentRegister.setStatus(_A)
_EtsysPimExtNbrMgrNumSentRegisterStop_Type=Counter32
_EtsysPimExtNbrMgrNumSentRegisterStop_Object=MibTableColumn
etsysPimExtNbrMgrNumSentRegisterStop=_EtsysPimExtNbrMgrNumSentRegisterStop_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,6),_EtsysPimExtNbrMgrNumSentRegisterStop_Type())
etsysPimExtNbrMgrNumSentRegisterStop.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrMgrNumSentRegisterStop.setStatus(_A)
_EtsysPimExtNbrMgrNumRecvCRPAdvert_Type=Counter32
_EtsysPimExtNbrMgrNumRecvCRPAdvert_Object=MibTableColumn
etsysPimExtNbrMgrNumRecvCRPAdvert=_EtsysPimExtNbrMgrNumRecvCRPAdvert_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,7),_EtsysPimExtNbrMgrNumRecvCRPAdvert_Type())
etsysPimExtNbrMgrNumRecvCRPAdvert.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrMgrNumRecvCRPAdvert.setStatus(_A)
_EtsysPimExtNbrMgrNumRecvRegister_Type=Counter32
_EtsysPimExtNbrMgrNumRecvRegister_Object=MibTableColumn
etsysPimExtNbrMgrNumRecvRegister=_EtsysPimExtNbrMgrNumRecvRegister_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,8),_EtsysPimExtNbrMgrNumRecvRegister_Type())
etsysPimExtNbrMgrNumRecvRegister.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrMgrNumRecvRegister.setStatus(_A)
_EtsysPimExtNbrMgrNumRecvRegisterStop_Type=Counter32
_EtsysPimExtNbrMgrNumRecvRegisterStop_Object=MibTableColumn
etsysPimExtNbrMgrNumRecvRegisterStop=_EtsysPimExtNbrMgrNumRecvRegisterStop_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,9),_EtsysPimExtNbrMgrNumRecvRegisterStop_Type())
etsysPimExtNbrMgrNumRecvRegisterStop.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrMgrNumRecvRegisterStop.setStatus(_A)
_EtsysPimExtNbrMgrNumErrCRPAdvert_Type=Counter32
_EtsysPimExtNbrMgrNumErrCRPAdvert_Object=MibTableColumn
etsysPimExtNbrMgrNumErrCRPAdvert=_EtsysPimExtNbrMgrNumErrCRPAdvert_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,10),_EtsysPimExtNbrMgrNumErrCRPAdvert_Type())
etsysPimExtNbrMgrNumErrCRPAdvert.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrMgrNumErrCRPAdvert.setStatus(_A)
_EtsysPimExtNbrMgrNumErrRegister_Type=Counter32
_EtsysPimExtNbrMgrNumErrRegister_Object=MibTableColumn
etsysPimExtNbrMgrNumErrRegister=_EtsysPimExtNbrMgrNumErrRegister_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,11),_EtsysPimExtNbrMgrNumErrRegister_Type())
etsysPimExtNbrMgrNumErrRegister.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrMgrNumErrRegister.setStatus(_A)
_EtsysPimExtNbrMgrNumErrRegisterStop_Type=Counter32
_EtsysPimExtNbrMgrNumErrRegisterStop_Object=MibTableColumn
etsysPimExtNbrMgrNumErrRegisterStop=_EtsysPimExtNbrMgrNumErrRegisterStop_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,12),_EtsysPimExtNbrMgrNumErrRegisterStop_Type())
etsysPimExtNbrMgrNumErrRegisterStop.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrMgrNumErrRegisterStop.setStatus(_A)
_EtsysPimExtNbrMgrNumRecvIgnoredType_Type=Counter32
_EtsysPimExtNbrMgrNumRecvIgnoredType_Object=MibTableColumn
etsysPimExtNbrMgrNumRecvIgnoredType=_EtsysPimExtNbrMgrNumRecvIgnoredType_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,13),_EtsysPimExtNbrMgrNumRecvIgnoredType_Type())
etsysPimExtNbrMgrNumRecvIgnoredType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrMgrNumRecvIgnoredType.setStatus(_A)
_EtsysPimExtNbrMgrNumRecvUnknownType_Type=Counter32
_EtsysPimExtNbrMgrNumRecvUnknownType_Object=MibTableColumn
etsysPimExtNbrMgrNumRecvUnknownType=_EtsysPimExtNbrMgrNumRecvUnknownType_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,14),_EtsysPimExtNbrMgrNumRecvUnknownType_Type())
etsysPimExtNbrMgrNumRecvUnknownType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrMgrNumRecvUnknownType.setStatus(_A)
_EtsysPimExtNbrMgrNumRecvUnknownVer_Type=Counter32
_EtsysPimExtNbrMgrNumRecvUnknownVer_Object=MibTableColumn
etsysPimExtNbrMgrNumRecvUnknownVer=_EtsysPimExtNbrMgrNumRecvUnknownVer_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,15),_EtsysPimExtNbrMgrNumRecvUnknownVer_Type())
etsysPimExtNbrMgrNumRecvUnknownVer.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrMgrNumRecvUnknownVer.setStatus(_A)
_EtsysPimExtNbrMgrNumRecvBadChecksum_Type=Counter32
_EtsysPimExtNbrMgrNumRecvBadChecksum_Object=MibTableColumn
etsysPimExtNbrMgrNumRecvBadChecksum=_EtsysPimExtNbrMgrNumRecvBadChecksum_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,16),_EtsysPimExtNbrMgrNumRecvBadChecksum_Type())
etsysPimExtNbrMgrNumRecvBadChecksum.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrMgrNumRecvBadChecksum.setStatus(_A)
_EtsysPimExtNbrMgrNumRecvBadLength_Type=Counter32
_EtsysPimExtNbrMgrNumRecvBadLength_Object=MibTableColumn
etsysPimExtNbrMgrNumRecvBadLength=_EtsysPimExtNbrMgrNumRecvBadLength_Object((1,3,6,1,4,1,5624,1,2,67,1,2,7,1,17),_EtsysPimExtNbrMgrNumRecvBadLength_Type())
etsysPimExtNbrMgrNumRecvBadLength.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtNbrMgrNumRecvBadLength.setStatus(_A)
_EtsysPimExtTibMgrTable_Object=MibTable
etsysPimExtTibMgrTable=_EtsysPimExtTibMgrTable_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8))
if mibBuilder.loadTexts:etsysPimExtTibMgrTable.setStatus(_A)
_EtsysPimExtTibMgrEntry_Object=MibTableRow
etsysPimExtTibMgrEntry=_EtsysPimExtTibMgrEntry_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1))
etsysPimExtTibMgrEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:etsysPimExtTibMgrEntry.setStatus(_A)
_EtsysPimExtTibMgrIndex_Type=InetVersion
_EtsysPimExtTibMgrIndex_Object=MibTableColumn
etsysPimExtTibMgrIndex=_EtsysPimExtTibMgrIndex_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,1),_EtsysPimExtTibMgrIndex_Type())
etsysPimExtTibMgrIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:etsysPimExtTibMgrIndex.setStatus(_A)
class _EtsysPimExtTibMgrGStateLimit_Type(Unsigned32):defaultValue=0
_EtsysPimExtTibMgrGStateLimit_Type.__name__=_D
_EtsysPimExtTibMgrGStateLimit_Object=MibTableColumn
etsysPimExtTibMgrGStateLimit=_EtsysPimExtTibMgrGStateLimit_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,2),_EtsysPimExtTibMgrGStateLimit_Type())
etsysPimExtTibMgrGStateLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPimExtTibMgrGStateLimit.setStatus(_A)
class _EtsysPimExtTibMgrGStateWarnThold_Type(Unsigned32):defaultValue=0
_EtsysPimExtTibMgrGStateWarnThold_Type.__name__=_D
_EtsysPimExtTibMgrGStateWarnThold_Object=MibTableColumn
etsysPimExtTibMgrGStateWarnThold=_EtsysPimExtTibMgrGStateWarnThold_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,3),_EtsysPimExtTibMgrGStateWarnThold_Type())
etsysPimExtTibMgrGStateWarnThold.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPimExtTibMgrGStateWarnThold.setStatus(_A)
_EtsysPimExtTibMgrGStateStored_Type=Gauge32
_EtsysPimExtTibMgrGStateStored_Object=MibTableColumn
etsysPimExtTibMgrGStateStored=_EtsysPimExtTibMgrGStateStored_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,4),_EtsysPimExtTibMgrGStateStored_Type())
etsysPimExtTibMgrGStateStored.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtTibMgrGStateStored.setStatus(_A)
class _EtsysPimExtTibMgrSGStateLimit_Type(Unsigned32):defaultValue=0
_EtsysPimExtTibMgrSGStateLimit_Type.__name__=_D
_EtsysPimExtTibMgrSGStateLimit_Object=MibTableColumn
etsysPimExtTibMgrSGStateLimit=_EtsysPimExtTibMgrSGStateLimit_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,5),_EtsysPimExtTibMgrSGStateLimit_Type())
etsysPimExtTibMgrSGStateLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPimExtTibMgrSGStateLimit.setStatus(_A)
class _EtsysPimExtTibMgrSGStateWarnThold_Type(Unsigned32):defaultValue=0
_EtsysPimExtTibMgrSGStateWarnThold_Type.__name__=_D
_EtsysPimExtTibMgrSGStateWarnThold_Object=MibTableColumn
etsysPimExtTibMgrSGStateWarnThold=_EtsysPimExtTibMgrSGStateWarnThold_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,6),_EtsysPimExtTibMgrSGStateWarnThold_Type())
etsysPimExtTibMgrSGStateWarnThold.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPimExtTibMgrSGStateWarnThold.setStatus(_A)
_EtsysPimExtTibMgrSGStateStored_Type=Gauge32
_EtsysPimExtTibMgrSGStateStored_Object=MibTableColumn
etsysPimExtTibMgrSGStateStored=_EtsysPimExtTibMgrSGStateStored_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,7),_EtsysPimExtTibMgrSGStateStored_Type())
etsysPimExtTibMgrSGStateStored.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtTibMgrSGStateStored.setStatus(_A)
class _EtsysPimExtTibMgrStarGIStateLimit_Type(Unsigned32):defaultValue=0
_EtsysPimExtTibMgrStarGIStateLimit_Type.__name__=_D
_EtsysPimExtTibMgrStarGIStateLimit_Object=MibTableColumn
etsysPimExtTibMgrStarGIStateLimit=_EtsysPimExtTibMgrStarGIStateLimit_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,8),_EtsysPimExtTibMgrStarGIStateLimit_Type())
etsysPimExtTibMgrStarGIStateLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPimExtTibMgrStarGIStateLimit.setStatus(_A)
class _EtsysPimExtTibMgrStarGIStateWarnThold_Type(Unsigned32):defaultValue=0
_EtsysPimExtTibMgrStarGIStateWarnThold_Type.__name__=_D
_EtsysPimExtTibMgrStarGIStateWarnThold_Object=MibTableColumn
etsysPimExtTibMgrStarGIStateWarnThold=_EtsysPimExtTibMgrStarGIStateWarnThold_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,9),_EtsysPimExtTibMgrStarGIStateWarnThold_Type())
etsysPimExtTibMgrStarGIStateWarnThold.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPimExtTibMgrStarGIStateWarnThold.setStatus(_A)
_EtsysPimExtTibMgrStarGIStateStored_Type=Gauge32
_EtsysPimExtTibMgrStarGIStateStored_Object=MibTableColumn
etsysPimExtTibMgrStarGIStateStored=_EtsysPimExtTibMgrStarGIStateStored_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,10),_EtsysPimExtTibMgrStarGIStateStored_Type())
etsysPimExtTibMgrStarGIStateStored.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtTibMgrStarGIStateStored.setStatus(_A)
class _EtsysPimExtTibMgrSGIStateLimit_Type(Unsigned32):defaultValue=0
_EtsysPimExtTibMgrSGIStateLimit_Type.__name__=_D
_EtsysPimExtTibMgrSGIStateLimit_Object=MibTableColumn
etsysPimExtTibMgrSGIStateLimit=_EtsysPimExtTibMgrSGIStateLimit_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,11),_EtsysPimExtTibMgrSGIStateLimit_Type())
etsysPimExtTibMgrSGIStateLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPimExtTibMgrSGIStateLimit.setStatus(_A)
class _EtsysPimExtTibMgrSGIStateWarnThold_Type(Unsigned32):defaultValue=0
_EtsysPimExtTibMgrSGIStateWarnThold_Type.__name__=_D
_EtsysPimExtTibMgrSGIStateWarnThold_Object=MibTableColumn
etsysPimExtTibMgrSGIStateWarnThold=_EtsysPimExtTibMgrSGIStateWarnThold_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,12),_EtsysPimExtTibMgrSGIStateWarnThold_Type())
etsysPimExtTibMgrSGIStateWarnThold.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPimExtTibMgrSGIStateWarnThold.setStatus(_A)
_EtsysPimExtTibMgrSGIStateStored_Type=Gauge32
_EtsysPimExtTibMgrSGIStateStored_Object=MibTableColumn
etsysPimExtTibMgrSGIStateStored=_EtsysPimExtTibMgrSGIStateStored_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,13),_EtsysPimExtTibMgrSGIStateStored_Type())
etsysPimExtTibMgrSGIStateStored.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPimExtTibMgrSGIStateStored.setStatus(_A)
class _EtsysPimExtTibMgrRegSuppressionTime_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EtsysPimExtTibMgrRegSuppressionTime_Type.__name__=_D
_EtsysPimExtTibMgrRegSuppressionTime_Object=MibTableColumn
etsysPimExtTibMgrRegSuppressionTime=_EtsysPimExtTibMgrRegSuppressionTime_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,14),_EtsysPimExtTibMgrRegSuppressionTime_Type())
etsysPimExtTibMgrRegSuppressionTime.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPimExtTibMgrRegSuppressionTime.setStatus(_A)
if mibBuilder.loadTexts:etsysPimExtTibMgrRegSuppressionTime.setUnits(_H)
class _EtsysPimExtTibMgrRegProbeTime_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EtsysPimExtTibMgrRegProbeTime_Type.__name__=_D
_EtsysPimExtTibMgrRegProbeTime_Object=MibTableColumn
etsysPimExtTibMgrRegProbeTime=_EtsysPimExtTibMgrRegProbeTime_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,15),_EtsysPimExtTibMgrRegProbeTime_Type())
etsysPimExtTibMgrRegProbeTime.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPimExtTibMgrRegProbeTime.setStatus(_A)
if mibBuilder.loadTexts:etsysPimExtTibMgrRegProbeTime.setUnits(_H)
class _EtsysPimExtTibMgrKeepalivePeriod_Type(Unsigned32):defaultValue=210;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EtsysPimExtTibMgrKeepalivePeriod_Type.__name__=_D
_EtsysPimExtTibMgrKeepalivePeriod_Object=MibTableColumn
etsysPimExtTibMgrKeepalivePeriod=_EtsysPimExtTibMgrKeepalivePeriod_Object((1,3,6,1,4,1,5624,1,2,67,1,2,8,1,16),_EtsysPimExtTibMgrKeepalivePeriod_Type())
etsysPimExtTibMgrKeepalivePeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPimExtTibMgrKeepalivePeriod.setStatus(_A)
if mibBuilder.loadTexts:etsysPimExtTibMgrKeepalivePeriod.setUnits(_H)
_EtsysPimExtConformance_ObjectIdentity=ObjectIdentity
etsysPimExtConformance=_EtsysPimExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,67,3))
_EtsysPimExtGroups_ObjectIdentity=ObjectIdentity
etsysPimExtGroups=_EtsysPimExtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,67,3,1))
_EtsysPimExtCompliances_ObjectIdentity=ObjectIdentity
etsysPimExtCompliances=_EtsysPimExtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,67,3,2))
pimInterfaceEntry.registerAugmentions((_B,_O))
etsysPimExtIfEntry.setIndexNames(*pimInterfaceEntry.getIndexNames())
pimStaticRPEntry.registerAugmentions((_B,_P))
etsysPimExtStaticRPEntry.setIndexNames(*pimStaticRPEntry.getIndexNames())
pimAnycastRPSetEntry.registerAugmentions((_B,_Q))
etsysPimExtAnycastRPSetEntry.setIndexNames(*pimAnycastRPSetEntry.getIndexNames())
pimGroupMappingEntry.registerAugmentions((_B,_R))
etsysPimExtGroupMappingEntry.setIndexNames(*pimGroupMappingEntry.getIndexNames())
pimNeighborEntry.registerAugmentions((_B,_S))
etsysPimExtNbrStatsEntry.setIndexNames(*pimNeighborEntry.getIndexNames())
pimInterfaceEntry.registerAugmentions((_B,_T))
etsysPimExtIfStatsEntry.setIndexNames(*pimInterfaceEntry.getIndexNames())
etsysPimExtIfGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,67,3,1,1))
etsysPimExtIfGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:etsysPimExtIfGroup.setStatus(_A)
etsysPimExtStaticRPGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,67,3,1,2))
etsysPimExtStaticRPGroup.setObjects((_B,_g))
if mibBuilder.loadTexts:etsysPimExtStaticRPGroup.setStatus(_A)
etsysPimExtAnycastRPSetGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,67,3,1,3))
etsysPimExtAnycastRPSetGroup.setObjects((_B,_h))
if mibBuilder.loadTexts:etsysPimExtAnycastRPSetGroup.setStatus(_A)
etsysPimExtGroupMappingGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,67,3,1,4))
etsysPimExtGroupMappingGroup.setObjects((_B,_i))
if mibBuilder.loadTexts:etsysPimExtGroupMappingGroup.setStatus(_A)
etsysPimExtNbrStatsGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,67,3,1,5))
etsysPimExtNbrStatsGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:etsysPimExtNbrStatsGroup.setStatus(_A)
etsysPimExtIfStatsGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,67,3,1,6))
etsysPimExtIfStatsGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:etsysPimExtIfStatsGroup.setStatus(_A)
etsysPimExtNbrMgrGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,67,3,1,7))
etsysPimExtNbrMgrGroup.setObjects(*((_B,_L),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:etsysPimExtNbrMgrGroup.setStatus(_A)
etsysPimExtTibMgrGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,67,3,1,8))
etsysPimExtTibMgrGroup.setObjects(*((_B,_M),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:etsysPimExtTibMgrGroup.setStatus(_A)
etsysPimExtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,67,3,2,1))
etsysPimExtCompliance.setObjects(*((_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:etsysPimExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysPimExtMIB':etsysPimExtMIB,'etsysPimExtObjects':etsysPimExtObjects,'etsysPimExtGlobals':etsysPimExtGlobals,'etsysPimExtTables':etsysPimExtTables,'etsysPimExtIfTable':etsysPimExtIfTable,_O:etsysPimExtIfEntry,_U:etsysPimExtIfAdminStatus,_V:etsysPimExtIfOperStatus,_W:etsysPimExtIfP2PNoHellos,_X:etsysPimExtIfNeighborCount,_Y:etsysPimExtIfStarGStateLimit,_Z:etsysPimExtIfStarGStateWarnThold,_a:etsysPimExtIfStarGStateStored,_b:etsysPimExtIfSGStateLimit,_c:etsysPimExtIfSGStateWarnThold,_d:etsysPimExtIfSGStateStored,_e:etsysPimExtIfAssertInterval,_f:etsysPimExtIfAssertHoldtime,'etsysPimExtStaticRPTable':etsysPimExtStaticRPTable,_P:etsysPimExtStaticRPEntry,_g:etsysPimExtStaticRPAdminStatus,'etsysPimExtAnycastRPSetTable':etsysPimExtAnycastRPSetTable,_Q:etsysPimExtAnycastRPSetEntry,_h:etsysPimExtAnycastRPSetAdminStatus,'etsysPimExtGroupMappingTable':etsysPimExtGroupMappingTable,_R:etsysPimExtGroupMappingEntry,_i:etsysPimExtGroupMappingIsInactive,'etsysPimExtNbrStatsTable':etsysPimExtNbrStatsTable,_S:etsysPimExtNbrStatsEntry,_j:etsysPimExtNbrStatsNumRecvHello,_k:etsysPimExtNbrStatsNumRecvJoinPrune,_l:etsysPimExtNbrStatsNumRecvAssert,_m:etsysPimExtNbrStatsNumRecvBSM,_n:etsysPimExtNbrStatsNumErrJoinPrune,_o:etsysPimExtNbrStatsNumErrAssert,_p:etsysPimExtNbrStatsNumErrBSM,'etsysPimExtIfStatsTable':etsysPimExtIfStatsTable,_T:etsysPimExtIfStatsEntry,_q:etsysPimExtIfStatsNumSentHello,_r:etsysPimExtIfStatsNumSentJoinPrune,_s:etsysPimExtIfStatsNumSentAssert,_t:etsysPimExtIfStatsNumSentBsm,_u:etsysPimExtIfStatsNumErrHello,_v:etsysPimExtIfStatsNumRecvUnknownNbr,_w:etsysPimExtIfStatsNumUnknownHelloOpt,'etsysPimExtNbrMgrTable':etsysPimExtNbrMgrTable,'etsysPimExtNbrMgrEntry':etsysPimExtNbrMgrEntry,_L:etsysPimExtNbrMgrIndex,_x:etsysPimExtNbrMgrEnableUnicastMessages,_y:etsysPimExtNbrMgrAcceptUnicastBsms,_z:etsysPimExtNbrMgrNumSentCRPAdvert,_A0:etsysPimExtNbrMgrNumSentRegister,_A1:etsysPimExtNbrMgrNumSentRegisterStop,_A2:etsysPimExtNbrMgrNumRecvCRPAdvert,_A3:etsysPimExtNbrMgrNumRecvRegister,_A4:etsysPimExtNbrMgrNumRecvRegisterStop,_A5:etsysPimExtNbrMgrNumErrCRPAdvert,_A6:etsysPimExtNbrMgrNumErrRegister,_A7:etsysPimExtNbrMgrNumErrRegisterStop,_A8:etsysPimExtNbrMgrNumRecvIgnoredType,_A9:etsysPimExtNbrMgrNumRecvUnknownType,_AA:etsysPimExtNbrMgrNumRecvUnknownVer,_AB:etsysPimExtNbrMgrNumRecvBadChecksum,_AC:etsysPimExtNbrMgrNumRecvBadLength,'etsysPimExtTibMgrTable':etsysPimExtTibMgrTable,'etsysPimExtTibMgrEntry':etsysPimExtTibMgrEntry,_M:etsysPimExtTibMgrIndex,_AD:etsysPimExtTibMgrGStateLimit,_AE:etsysPimExtTibMgrGStateWarnThold,_AF:etsysPimExtTibMgrGStateStored,_AG:etsysPimExtTibMgrSGStateLimit,_AH:etsysPimExtTibMgrSGStateWarnThold,_AI:etsysPimExtTibMgrSGStateStored,_AJ:etsysPimExtTibMgrStarGIStateLimit,_AK:etsysPimExtTibMgrStarGIStateWarnThold,_AL:etsysPimExtTibMgrStarGIStateStored,_AM:etsysPimExtTibMgrSGIStateLimit,_AN:etsysPimExtTibMgrSGIStateWarnThold,_AO:etsysPimExtTibMgrSGIStateStored,_AP:etsysPimExtTibMgrRegSuppressionTime,_AQ:etsysPimExtTibMgrRegProbeTime,_AR:etsysPimExtTibMgrKeepalivePeriod,'etsysPimExtConformance':etsysPimExtConformance,'etsysPimExtGroups':etsysPimExtGroups,_AS:etsysPimExtIfGroup,_AT:etsysPimExtStaticRPGroup,_AU:etsysPimExtAnycastRPSetGroup,_AV:etsysPimExtGroupMappingGroup,_AW:etsysPimExtNbrStatsGroup,_AX:etsysPimExtIfStatsGroup,_AY:etsysPimExtNbrMgrGroup,_AZ:etsysPimExtTibMgrGroup,'etsysPimExtCompliances':etsysPimExtCompliances,'etsysPimExtCompliance':etsysPimExtCompliance})