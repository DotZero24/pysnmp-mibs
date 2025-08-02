_k='etsysEthOamExtUldConfigGroup'
_j='etsysEthOamExtEventConfigGroup'
_i='etsysEthOamExtGroup'
_h='etsysEthOamExtUldPortActiveOamMode'
_g='etsysEthOamExtUldPortGroupIndex'
_f='etsysEthOamExtUldPortLastFastRxTime'
_e='etsysEthOamExtUldPortFastRxErrorCount'
_d='etsysEthOamExtUldPortFastRxCount'
_c='etsysEthOamExtUldPortFastTxCount'
_b='etsysEthOamExtUldPortOperStatus'
_a='etsysEthOamExtUldPortActiveFastStatus'
_Z='etsysEthOamExtUldPortActiveFastTimer'
_Y='etsysEthOamExtUldPortFastTimerConfig'
_X='etsysEthOamExtUldPortActiveStatus'
_W='etsysEthOamExtUldPortAction'
_V='etsysEthOamExtUldPortMode'
_U='etsysEthOamExtUldGroupFastPortsInUse'
_T='etsysEthOamExtUldGroupMaxFastPorts'
_S='etsysEthOamExtEventConfigErrNotifRetry'
_R='etsysEthOamExtEventConfigErrFrameSecsActions'
_Q='etsysEthOamExtEventConfigErrFrameActions'
_P='etsysEthOamExtEventConfigErrFramePeriodActions'
_O='etsysEthOamExtEventConfigErrSymPeriodActions'
_N='etsysEthOamExtOperStatus'
_M='deciseconds'
_L='etsysEthOamExtUldGroupIndex'
_K='operational'
_J='disabled'
_I='Unsigned32'
_H='ifIndex'
_G='IF-MIB'
_F='EtsysOamExtErrActions'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='ENTERASYS-ETH-OAM-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
etsysEthOamExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,78))
if mibBuilder.loadTexts:etsysEthOamExtMIB.setRevisions(('2012-02-07 14:54','2010-11-23 19:00'))
class EtsysOamExtErrActions(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('syslog',0),('disable',1)))
_EtsysEthOamExtObjects_ObjectIdentity=ObjectIdentity
etsysEthOamExtObjects=_EtsysEthOamExtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,78,1))
_EtsysEthOamExtTable_Object=MibTable
etsysEthOamExtTable=_EtsysEthOamExtTable_Object((1,3,6,1,4,1,5624,1,2,78,1,1))
if mibBuilder.loadTexts:etsysEthOamExtTable.setStatus(_A)
_EtsysEthOamExtEntry_Object=MibTableRow
etsysEthOamExtEntry=_EtsysEthOamExtEntry_Object((1,3,6,1,4,1,5624,1,2,78,1,1,1))
etsysEthOamExtEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:etsysEthOamExtEntry.setStatus(_A)
class _EtsysEthOamExtOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_EtsysEthOamExtOperStatus_Type.__name__=_E
_EtsysEthOamExtOperStatus_Object=MibTableColumn
etsysEthOamExtOperStatus=_EtsysEthOamExtOperStatus_Object((1,3,6,1,4,1,5624,1,2,78,1,1,1,1),_EtsysEthOamExtOperStatus_Type())
etsysEthOamExtOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEthOamExtOperStatus.setStatus(_A)
_EtsysEthOamExtEventConfigTable_Object=MibTable
etsysEthOamExtEventConfigTable=_EtsysEthOamExtEventConfigTable_Object((1,3,6,1,4,1,5624,1,2,78,1,2))
if mibBuilder.loadTexts:etsysEthOamExtEventConfigTable.setStatus(_A)
_EtsysEthOamExtEventConfigEntry_Object=MibTableRow
etsysEthOamExtEventConfigEntry=_EtsysEthOamExtEventConfigEntry_Object((1,3,6,1,4,1,5624,1,2,78,1,2,1))
etsysEthOamExtEventConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:etsysEthOamExtEventConfigEntry.setStatus(_A)
class _EtsysEthOamExtEventConfigErrSymPeriodActions_Type(EtsysOamExtErrActions):defaultHexValue=''
_EtsysEthOamExtEventConfigErrSymPeriodActions_Type.__name__=_F
_EtsysEthOamExtEventConfigErrSymPeriodActions_Object=MibTableColumn
etsysEthOamExtEventConfigErrSymPeriodActions=_EtsysEthOamExtEventConfigErrSymPeriodActions_Object((1,3,6,1,4,1,5624,1,2,78,1,2,1,1),_EtsysEthOamExtEventConfigErrSymPeriodActions_Type())
etsysEthOamExtEventConfigErrSymPeriodActions.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEthOamExtEventConfigErrSymPeriodActions.setStatus(_A)
class _EtsysEthOamExtEventConfigErrFramePeriodActions_Type(EtsysOamExtErrActions):defaultHexValue=''
_EtsysEthOamExtEventConfigErrFramePeriodActions_Type.__name__=_F
_EtsysEthOamExtEventConfigErrFramePeriodActions_Object=MibTableColumn
etsysEthOamExtEventConfigErrFramePeriodActions=_EtsysEthOamExtEventConfigErrFramePeriodActions_Object((1,3,6,1,4,1,5624,1,2,78,1,2,1,2),_EtsysEthOamExtEventConfigErrFramePeriodActions_Type())
etsysEthOamExtEventConfigErrFramePeriodActions.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEthOamExtEventConfigErrFramePeriodActions.setStatus(_A)
class _EtsysEthOamExtEventConfigErrFrameActions_Type(EtsysOamExtErrActions):defaultHexValue=''
_EtsysEthOamExtEventConfigErrFrameActions_Type.__name__=_F
_EtsysEthOamExtEventConfigErrFrameActions_Object=MibTableColumn
etsysEthOamExtEventConfigErrFrameActions=_EtsysEthOamExtEventConfigErrFrameActions_Object((1,3,6,1,4,1,5624,1,2,78,1,2,1,3),_EtsysEthOamExtEventConfigErrFrameActions_Type())
etsysEthOamExtEventConfigErrFrameActions.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEthOamExtEventConfigErrFrameActions.setStatus(_A)
class _EtsysEthOamExtEventConfigErrFrameSecsActions_Type(EtsysOamExtErrActions):defaultHexValue=''
_EtsysEthOamExtEventConfigErrFrameSecsActions_Type.__name__=_F
_EtsysEthOamExtEventConfigErrFrameSecsActions_Object=MibTableColumn
etsysEthOamExtEventConfigErrFrameSecsActions=_EtsysEthOamExtEventConfigErrFrameSecsActions_Object((1,3,6,1,4,1,5624,1,2,78,1,2,1,4),_EtsysEthOamExtEventConfigErrFrameSecsActions_Type())
etsysEthOamExtEventConfigErrFrameSecsActions.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEthOamExtEventConfigErrFrameSecsActions.setStatus(_A)
class _EtsysEthOamExtEventConfigErrNotifRetry_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_EtsysEthOamExtEventConfigErrNotifRetry_Type.__name__=_I
_EtsysEthOamExtEventConfigErrNotifRetry_Object=MibTableColumn
etsysEthOamExtEventConfigErrNotifRetry=_EtsysEthOamExtEventConfigErrNotifRetry_Object((1,3,6,1,4,1,5624,1,2,78,1,2,1,5),_EtsysEthOamExtEventConfigErrNotifRetry_Type())
etsysEthOamExtEventConfigErrNotifRetry.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEthOamExtEventConfigErrNotifRetry.setStatus(_A)
_EtsysEthOamExtUld_ObjectIdentity=ObjectIdentity
etsysEthOamExtUld=_EtsysEthOamExtUld_ObjectIdentity((1,3,6,1,4,1,5624,1,2,78,1,3))
_EtsysEthOamExtUldGroupTable_Object=MibTable
etsysEthOamExtUldGroupTable=_EtsysEthOamExtUldGroupTable_Object((1,3,6,1,4,1,5624,1,2,78,1,3,1))
if mibBuilder.loadTexts:etsysEthOamExtUldGroupTable.setStatus(_A)
_EtsysEthOamExtUldGroupEntry_Object=MibTableRow
etsysEthOamExtUldGroupEntry=_EtsysEthOamExtUldGroupEntry_Object((1,3,6,1,4,1,5624,1,2,78,1,3,1,1))
etsysEthOamExtUldGroupEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:etsysEthOamExtUldGroupEntry.setStatus(_A)
_EtsysEthOamExtUldGroupIndex_Type=Unsigned32
_EtsysEthOamExtUldGroupIndex_Object=MibTableColumn
etsysEthOamExtUldGroupIndex=_EtsysEthOamExtUldGroupIndex_Object((1,3,6,1,4,1,5624,1,2,78,1,3,1,1,1),_EtsysEthOamExtUldGroupIndex_Type())
etsysEthOamExtUldGroupIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsysEthOamExtUldGroupIndex.setStatus(_A)
_EtsysEthOamExtUldGroupMaxFastPorts_Type=Unsigned32
_EtsysEthOamExtUldGroupMaxFastPorts_Object=MibTableColumn
etsysEthOamExtUldGroupMaxFastPorts=_EtsysEthOamExtUldGroupMaxFastPorts_Object((1,3,6,1,4,1,5624,1,2,78,1,3,1,1,2),_EtsysEthOamExtUldGroupMaxFastPorts_Type())
etsysEthOamExtUldGroupMaxFastPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysEthOamExtUldGroupMaxFastPorts.setStatus(_A)
_EtsysEthOamExtUldGroupFastPortsInUse_Type=Gauge32
_EtsysEthOamExtUldGroupFastPortsInUse_Object=MibTableColumn
etsysEthOamExtUldGroupFastPortsInUse=_EtsysEthOamExtUldGroupFastPortsInUse_Object((1,3,6,1,4,1,5624,1,2,78,1,3,1,1,3),_EtsysEthOamExtUldGroupFastPortsInUse_Type())
etsysEthOamExtUldGroupFastPortsInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysEthOamExtUldGroupFastPortsInUse.setStatus(_A)
_EtsysEthOamExtUldPortTable_Object=MibTable
etsysEthOamExtUldPortTable=_EtsysEthOamExtUldPortTable_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2))
if mibBuilder.loadTexts:etsysEthOamExtUldPortTable.setStatus(_A)
_EtsysEthOamExtUldPortEntry_Object=MibTableRow
etsysEthOamExtUldPortEntry=_EtsysEthOamExtUldPortEntry_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2,1))
etsysEthOamExtUldPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:etsysEthOamExtUldPortEntry.setStatus(_A)
class _EtsysEthOamExtUldPortMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('standard',2),('fast',3)))
_EtsysEthOamExtUldPortMode_Type.__name__=_E
_EtsysEthOamExtUldPortMode_Object=MibTableColumn
etsysEthOamExtUldPortMode=_EtsysEthOamExtUldPortMode_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2,1,1),_EtsysEthOamExtUldPortMode_Type())
etsysEthOamExtUldPortMode.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEthOamExtUldPortMode.setStatus(_A)
class _EtsysEthOamExtUldPortAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('syslogOnly',1),('disablePort',2)))
_EtsysEthOamExtUldPortAction_Type.__name__=_E
_EtsysEthOamExtUldPortAction_Object=MibTableColumn
etsysEthOamExtUldPortAction=_EtsysEthOamExtUldPortAction_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2,1,2),_EtsysEthOamExtUldPortAction_Type())
etsysEthOamExtUldPortAction.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEthOamExtUldPortAction.setStatus(_A)
_EtsysEthOamExtUldPortActiveStatus_Type=TruthValue
_EtsysEthOamExtUldPortActiveStatus_Object=MibTableColumn
etsysEthOamExtUldPortActiveStatus=_EtsysEthOamExtUldPortActiveStatus_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2,1,3),_EtsysEthOamExtUldPortActiveStatus_Type())
etsysEthOamExtUldPortActiveStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysEthOamExtUldPortActiveStatus.setStatus(_A)
class _EtsysEthOamExtUldPortFastTimerConfig_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_EtsysEthOamExtUldPortFastTimerConfig_Type.__name__=_I
_EtsysEthOamExtUldPortFastTimerConfig_Object=MibTableColumn
etsysEthOamExtUldPortFastTimerConfig=_EtsysEthOamExtUldPortFastTimerConfig_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2,1,4),_EtsysEthOamExtUldPortFastTimerConfig_Type())
etsysEthOamExtUldPortFastTimerConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEthOamExtUldPortFastTimerConfig.setStatus(_A)
if mibBuilder.loadTexts:etsysEthOamExtUldPortFastTimerConfig.setUnits(_M)
_EtsysEthOamExtUldPortActiveFastTimer_Type=Unsigned32
_EtsysEthOamExtUldPortActiveFastTimer_Object=MibTableColumn
etsysEthOamExtUldPortActiveFastTimer=_EtsysEthOamExtUldPortActiveFastTimer_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2,1,5),_EtsysEthOamExtUldPortActiveFastTimer_Type())
etsysEthOamExtUldPortActiveFastTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysEthOamExtUldPortActiveFastTimer.setStatus(_A)
if mibBuilder.loadTexts:etsysEthOamExtUldPortActiveFastTimer.setUnits(_M)
class _EtsysEthOamExtUldPortActiveFastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notActive',1),('activeSlow',2),('activeFast',3),('faultDetected',4)))
_EtsysEthOamExtUldPortActiveFastStatus_Type.__name__=_E
_EtsysEthOamExtUldPortActiveFastStatus_Object=MibTableColumn
etsysEthOamExtUldPortActiveFastStatus=_EtsysEthOamExtUldPortActiveFastStatus_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2,1,6),_EtsysEthOamExtUldPortActiveFastStatus_Type())
etsysEthOamExtUldPortActiveFastStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysEthOamExtUldPortActiveFastStatus.setStatus(_A)
class _EtsysEthOamExtUldPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_EtsysEthOamExtUldPortOperStatus_Type.__name__=_E
_EtsysEthOamExtUldPortOperStatus_Object=MibTableColumn
etsysEthOamExtUldPortOperStatus=_EtsysEthOamExtUldPortOperStatus_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2,1,7),_EtsysEthOamExtUldPortOperStatus_Type())
etsysEthOamExtUldPortOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysEthOamExtUldPortOperStatus.setStatus(_A)
_EtsysEthOamExtUldPortFastTxCount_Type=Counter32
_EtsysEthOamExtUldPortFastTxCount_Object=MibTableColumn
etsysEthOamExtUldPortFastTxCount=_EtsysEthOamExtUldPortFastTxCount_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2,1,8),_EtsysEthOamExtUldPortFastTxCount_Type())
etsysEthOamExtUldPortFastTxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysEthOamExtUldPortFastTxCount.setStatus(_A)
_EtsysEthOamExtUldPortFastRxCount_Type=Counter32
_EtsysEthOamExtUldPortFastRxCount_Object=MibTableColumn
etsysEthOamExtUldPortFastRxCount=_EtsysEthOamExtUldPortFastRxCount_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2,1,9),_EtsysEthOamExtUldPortFastRxCount_Type())
etsysEthOamExtUldPortFastRxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysEthOamExtUldPortFastRxCount.setStatus(_A)
_EtsysEthOamExtUldPortFastRxErrorCount_Type=Counter32
_EtsysEthOamExtUldPortFastRxErrorCount_Object=MibTableColumn
etsysEthOamExtUldPortFastRxErrorCount=_EtsysEthOamExtUldPortFastRxErrorCount_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2,1,10),_EtsysEthOamExtUldPortFastRxErrorCount_Type())
etsysEthOamExtUldPortFastRxErrorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysEthOamExtUldPortFastRxErrorCount.setStatus(_A)
_EtsysEthOamExtUldPortLastFastRxTime_Type=TimeTicks
_EtsysEthOamExtUldPortLastFastRxTime_Object=MibTableColumn
etsysEthOamExtUldPortLastFastRxTime=_EtsysEthOamExtUldPortLastFastRxTime_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2,1,11),_EtsysEthOamExtUldPortLastFastRxTime_Type())
etsysEthOamExtUldPortLastFastRxTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysEthOamExtUldPortLastFastRxTime.setStatus(_A)
_EtsysEthOamExtUldPortGroupIndex_Type=Unsigned32
_EtsysEthOamExtUldPortGroupIndex_Object=MibTableColumn
etsysEthOamExtUldPortGroupIndex=_EtsysEthOamExtUldPortGroupIndex_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2,1,12),_EtsysEthOamExtUldPortGroupIndex_Type())
etsysEthOamExtUldPortGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysEthOamExtUldPortGroupIndex.setStatus(_A)
class _EtsysEthOamExtUldPortActiveOamMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('passive',1),('active',2)))
_EtsysEthOamExtUldPortActiveOamMode_Type.__name__=_E
_EtsysEthOamExtUldPortActiveOamMode_Object=MibTableColumn
etsysEthOamExtUldPortActiveOamMode=_EtsysEthOamExtUldPortActiveOamMode_Object((1,3,6,1,4,1,5624,1,2,78,1,3,2,1,13),_EtsysEthOamExtUldPortActiveOamMode_Type())
etsysEthOamExtUldPortActiveOamMode.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysEthOamExtUldPortActiveOamMode.setStatus(_A)
_EtsysEthOamExtConformance_ObjectIdentity=ObjectIdentity
etsysEthOamExtConformance=_EtsysEthOamExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,78,2))
_EtsysEthOamExtGroups_ObjectIdentity=ObjectIdentity
etsysEthOamExtGroups=_EtsysEthOamExtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,78,2,1))
_EtsysEthOamExtCompliances_ObjectIdentity=ObjectIdentity
etsysEthOamExtCompliances=_EtsysEthOamExtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,78,2,2))
etsysEthOamExtGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,78,2,1,1))
etsysEthOamExtGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:etsysEthOamExtGroup.setStatus(_A)
etsysEthOamExtEventConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,78,2,1,2))
etsysEthOamExtEventConfigGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:etsysEthOamExtEventConfigGroup.setStatus(_A)
etsysEthOamExtUldConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,78,2,1,3))
etsysEthOamExtUldConfigGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:etsysEthOamExtUldConfigGroup.setStatus(_A)
etsysEthOamExtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,78,2,2,1))
etsysEthOamExtCompliance.setObjects(*((_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:etsysEthOamExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_F:EtsysOamExtErrActions,'etsysEthOamExtMIB':etsysEthOamExtMIB,'etsysEthOamExtObjects':etsysEthOamExtObjects,'etsysEthOamExtTable':etsysEthOamExtTable,'etsysEthOamExtEntry':etsysEthOamExtEntry,_N:etsysEthOamExtOperStatus,'etsysEthOamExtEventConfigTable':etsysEthOamExtEventConfigTable,'etsysEthOamExtEventConfigEntry':etsysEthOamExtEventConfigEntry,_O:etsysEthOamExtEventConfigErrSymPeriodActions,_P:etsysEthOamExtEventConfigErrFramePeriodActions,_Q:etsysEthOamExtEventConfigErrFrameActions,_R:etsysEthOamExtEventConfigErrFrameSecsActions,_S:etsysEthOamExtEventConfigErrNotifRetry,'etsysEthOamExtUld':etsysEthOamExtUld,'etsysEthOamExtUldGroupTable':etsysEthOamExtUldGroupTable,'etsysEthOamExtUldGroupEntry':etsysEthOamExtUldGroupEntry,_L:etsysEthOamExtUldGroupIndex,_T:etsysEthOamExtUldGroupMaxFastPorts,_U:etsysEthOamExtUldGroupFastPortsInUse,'etsysEthOamExtUldPortTable':etsysEthOamExtUldPortTable,'etsysEthOamExtUldPortEntry':etsysEthOamExtUldPortEntry,_V:etsysEthOamExtUldPortMode,_W:etsysEthOamExtUldPortAction,_X:etsysEthOamExtUldPortActiveStatus,_Y:etsysEthOamExtUldPortFastTimerConfig,_Z:etsysEthOamExtUldPortActiveFastTimer,_a:etsysEthOamExtUldPortActiveFastStatus,_b:etsysEthOamExtUldPortOperStatus,_c:etsysEthOamExtUldPortFastTxCount,_d:etsysEthOamExtUldPortFastRxCount,_e:etsysEthOamExtUldPortFastRxErrorCount,_f:etsysEthOamExtUldPortLastFastRxTime,_g:etsysEthOamExtUldPortGroupIndex,_h:etsysEthOamExtUldPortActiveOamMode,'etsysEthOamExtConformance':etsysEthOamExtConformance,'etsysEthOamExtGroups':etsysEthOamExtGroups,_i:etsysEthOamExtGroup,_j:etsysEthOamExtEventConfigGroup,_k:etsysEthOamExtUldConfigGroup,'etsysEthOamExtCompliances':etsysEthOamExtCompliances,'etsysEthOamExtCompliance':etsysEthOamExtCompliance})