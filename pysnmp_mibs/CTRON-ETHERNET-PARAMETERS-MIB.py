_S='gigabit'
_R='hundredmegabit'
_Q='tenmegabit'
_P='asymmetricTx'
_O='asymmetricRx'
_N='symmetric'
_M='notsupported'
_L='enabled'
_K='fullduplex'
_J='halfduplex'
_I='unknown'
_H='ctIfPortPortNumber'
_G='ctIfPortIfNumber'
_F='disabled'
_E='read-write'
_D='CTIF-EXT-MIB'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctIfPortIfNumber,ctIfPortPortNumber=mibBuilder.importSymbols(_D,_G,_H)
ctEthernetCtlParameters,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctEthernetCtlParameters')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtAutoNegCtl_ObjectIdentity=ObjectIdentity
ctAutoNegCtl=_CtAutoNegCtl_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,4,2,1))
_CtAutoNegCtlTable_Object=MibTable
ctAutoNegCtlTable=_CtAutoNegCtlTable_Object((1,3,6,1,4,1,52,4,1,2,4,2,1,1))
if mibBuilder.loadTexts:ctAutoNegCtlTable.setStatus(_A)
_CtAutoNegCtlEntry_Object=MibTableRow
ctAutoNegCtlEntry=_CtAutoNegCtlEntry_Object((1,3,6,1,4,1,52,4,1,2,4,2,1,1,1))
ctAutoNegCtlEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:ctAutoNegCtlEntry.setStatus(_A)
class _CtAutoNegAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CtAutoNegAdminStatus_Type.__name__=_B
_CtAutoNegAdminStatus_Object=MibTableColumn
ctAutoNegAdminStatus=_CtAutoNegAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,4,2,1,1,1,1),_CtAutoNegAdminStatus_Type())
ctAutoNegAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctAutoNegAdminStatus.setStatus(_A)
class _CtAutoNegRemoteSignalling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('detected',1),('notdetected',2)))
_CtAutoNegRemoteSignalling_Type.__name__=_B
_CtAutoNegRemoteSignalling_Object=MibTableColumn
ctAutoNegRemoteSignalling=_CtAutoNegRemoteSignalling_Object((1,3,6,1,4,1,52,4,1,2,4,2,1,1,1,2),_CtAutoNegRemoteSignalling_Type())
ctAutoNegRemoteSignalling.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAutoNegRemoteSignalling.setStatus(_A)
class _CtAutoNegAutoConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('configuring',2),('complete',3),(_F,4),('paralleldetectfailed',5)))
_CtAutoNegAutoConfig_Type.__name__=_B
_CtAutoNegAutoConfig_Object=MibTableColumn
ctAutoNegAutoConfig=_CtAutoNegAutoConfig_Object((1,3,6,1,4,1,52,4,1,2,4,2,1,1,1,3),_CtAutoNegAutoConfig_Type())
ctAutoNegAutoConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAutoNegAutoConfig.setStatus(_A)
_CtAutoNegLocalTechnologyAbility_Type=Integer32
_CtAutoNegLocalTechnologyAbility_Object=MibTableColumn
ctAutoNegLocalTechnologyAbility=_CtAutoNegLocalTechnologyAbility_Object((1,3,6,1,4,1,52,4,1,2,4,2,1,1,1,4),_CtAutoNegLocalTechnologyAbility_Type())
ctAutoNegLocalTechnologyAbility.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAutoNegLocalTechnologyAbility.setStatus(_A)
_CtAutoNegAdvertisedTechnologyAbility_Type=Integer32
_CtAutoNegAdvertisedTechnologyAbility_Object=MibTableColumn
ctAutoNegAdvertisedTechnologyAbility=_CtAutoNegAdvertisedTechnologyAbility_Object((1,3,6,1,4,1,52,4,1,2,4,2,1,1,1,5),_CtAutoNegAdvertisedTechnologyAbility_Type())
ctAutoNegAdvertisedTechnologyAbility.setMaxAccess(_E)
if mibBuilder.loadTexts:ctAutoNegAdvertisedTechnologyAbility.setStatus(_A)
_CtAutoNegReceivedTechnologyAbility_Type=Integer32
_CtAutoNegReceivedTechnologyAbility_Object=MibTableColumn
ctAutoNegReceivedTechnologyAbility=_CtAutoNegReceivedTechnologyAbility_Object((1,3,6,1,4,1,52,4,1,2,4,2,1,1,1,6),_CtAutoNegReceivedTechnologyAbility_Type())
ctAutoNegReceivedTechnologyAbility.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAutoNegReceivedTechnologyAbility.setStatus(_A)
_CtFlowControl_ObjectIdentity=ObjectIdentity
ctFlowControl=_CtFlowControl_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,4,2,2))
_CtFlowCtlTable_Object=MibTable
ctFlowCtlTable=_CtFlowCtlTable_Object((1,3,6,1,4,1,52,4,1,2,4,2,2,1))
if mibBuilder.loadTexts:ctFlowCtlTable.setStatus(_A)
_CtFlowCtlEntry_Object=MibTableRow
ctFlowCtlEntry=_CtFlowCtlEntry_Object((1,3,6,1,4,1,52,4,1,2,4,2,2,1,1))
ctFlowCtlEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:ctFlowCtlEntry.setStatus(_A)
class _CtFlowCtlHalfDuplexAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_F,2)))
_CtFlowCtlHalfDuplexAdminStatus_Type.__name__=_B
_CtFlowCtlHalfDuplexAdminStatus_Object=MibTableColumn
ctFlowCtlHalfDuplexAdminStatus=_CtFlowCtlHalfDuplexAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,4,2,2,1,1,1),_CtFlowCtlHalfDuplexAdminStatus_Type())
ctFlowCtlHalfDuplexAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctFlowCtlHalfDuplexAdminStatus.setStatus(_A)
class _CtFlowCtlHalfDuplexOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_F,2),(_M,3)))
_CtFlowCtlHalfDuplexOperStatus_Type.__name__=_B
_CtFlowCtlHalfDuplexOperStatus_Object=MibTableColumn
ctFlowCtlHalfDuplexOperStatus=_CtFlowCtlHalfDuplexOperStatus_Object((1,3,6,1,4,1,52,4,1,2,4,2,2,1,1,2),_CtFlowCtlHalfDuplexOperStatus_Type())
ctFlowCtlHalfDuplexOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctFlowCtlHalfDuplexOperStatus.setStatus(_A)
_CtEtherSupportedPauseModes_Type=Integer32
_CtEtherSupportedPauseModes_Object=MibTableColumn
ctEtherSupportedPauseModes=_CtEtherSupportedPauseModes_Object((1,3,6,1,4,1,52,4,1,2,4,2,2,1,1,3),_CtEtherSupportedPauseModes_Type())
ctEtherSupportedPauseModes.setMaxAccess(_C)
if mibBuilder.loadTexts:ctEtherSupportedPauseModes.setStatus(_A)
class _CtFlowCtlPauseAdminStatus_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_F,4),('autonegotiate',5)))
_CtFlowCtlPauseAdminStatus_Type.__name__=_B
_CtFlowCtlPauseAdminStatus_Object=MibTableColumn
ctFlowCtlPauseAdminStatus=_CtFlowCtlPauseAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,4,2,2,1,1,4),_CtFlowCtlPauseAdminStatus_Type())
ctFlowCtlPauseAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctFlowCtlPauseAdminStatus.setStatus(_A)
class _CtFlowCtlPauseOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_F,4),(_I,5),(_M,6)))
_CtFlowCtlPauseOperStatus_Type.__name__=_B
_CtFlowCtlPauseOperStatus_Object=MibTableColumn
ctFlowCtlPauseOperStatus=_CtFlowCtlPauseOperStatus_Object((1,3,6,1,4,1,52,4,1,2,4,2,2,1,1,5),_CtFlowCtlPauseOperStatus_Type())
ctFlowCtlPauseOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctFlowCtlPauseOperStatus.setStatus(_A)
class _CtFlowCtlPauseTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CtFlowCtlPauseTimer_Type.__name__=_B
_CtFlowCtlPauseTimer_Object=MibTableColumn
ctFlowCtlPauseTimer=_CtFlowCtlPauseTimer_Object((1,3,6,1,4,1,52,4,1,2,4,2,2,1,1,6),_CtFlowCtlPauseTimer_Type())
ctFlowCtlPauseTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:ctFlowCtlPauseTimer.setStatus(_A)
_CtFlowCtlRxPauseFrames_Type=Counter32
_CtFlowCtlRxPauseFrames_Object=MibTableColumn
ctFlowCtlRxPauseFrames=_CtFlowCtlRxPauseFrames_Object((1,3,6,1,4,1,52,4,1,2,4,2,2,1,1,7),_CtFlowCtlRxPauseFrames_Type())
ctFlowCtlRxPauseFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ctFlowCtlRxPauseFrames.setStatus(_A)
_CtFlowCtlTxPauseFrames_Type=Counter32
_CtFlowCtlTxPauseFrames_Object=MibTableColumn
ctFlowCtlTxPauseFrames=_CtFlowCtlTxPauseFrames_Object((1,3,6,1,4,1,52,4,1,2,4,2,2,1,1,8),_CtFlowCtlTxPauseFrames_Type())
ctFlowCtlTxPauseFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ctFlowCtlTxPauseFrames.setStatus(_A)
_CtEtherManualConfig_ObjectIdentity=ObjectIdentity
ctEtherManualConfig=_CtEtherManualConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,4,2,3))
_CtEtherManualConfigTable_Object=MibTable
ctEtherManualConfigTable=_CtEtherManualConfigTable_Object((1,3,6,1,4,1,52,4,1,2,4,2,3,1))
if mibBuilder.loadTexts:ctEtherManualConfigTable.setStatus(_A)
_CtEtherManualConfigEntry_Object=MibTableRow
ctEtherManualConfigEntry=_CtEtherManualConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,4,2,3,1,1))
ctEtherManualConfigEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:ctEtherManualConfigEntry.setStatus(_A)
_CtEtherSupportedSpeed_Type=Integer32
_CtEtherSupportedSpeed_Object=MibTableColumn
ctEtherSupportedSpeed=_CtEtherSupportedSpeed_Object((1,3,6,1,4,1,52,4,1,2,4,2,3,1,1,1),_CtEtherSupportedSpeed_Type())
ctEtherSupportedSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:ctEtherSupportedSpeed.setStatus(_A)
class _CtEtherSpeedAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_Q,2),(_R,3),(_S,4)))
_CtEtherSpeedAdminStatus_Type.__name__=_B
_CtEtherSpeedAdminStatus_Object=MibTableColumn
ctEtherSpeedAdminStatus=_CtEtherSpeedAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,4,2,3,1,1,2),_CtEtherSpeedAdminStatus_Type())
ctEtherSpeedAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctEtherSpeedAdminStatus.setStatus(_A)
class _CtEtherSpeedOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_Q,2),(_R,3),(_S,4)))
_CtEtherSpeedOperStatus_Type.__name__=_B
_CtEtherSpeedOperStatus_Object=MibTableColumn
ctEtherSpeedOperStatus=_CtEtherSpeedOperStatus_Object((1,3,6,1,4,1,52,4,1,2,4,2,3,1,1,3),_CtEtherSpeedOperStatus_Type())
ctEtherSpeedOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctEtherSpeedOperStatus.setStatus(_A)
class _CtEtherSupportedDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),('halfandfullduplex',3)))
_CtEtherSupportedDuplex_Type.__name__=_B
_CtEtherSupportedDuplex_Object=MibTableColumn
ctEtherSupportedDuplex=_CtEtherSupportedDuplex_Object((1,3,6,1,4,1,52,4,1,2,4,2,3,1,1,4),_CtEtherSupportedDuplex_Type())
ctEtherSupportedDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctEtherSupportedDuplex.setStatus(_A)
class _CtEtherDuplexAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_J,2),(_K,3)))
_CtEtherDuplexAdminStatus_Type.__name__=_B
_CtEtherDuplexAdminStatus_Object=MibTableColumn
ctEtherDuplexAdminStatus=_CtEtherDuplexAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,4,2,3,1,1,5),_CtEtherDuplexAdminStatus_Type())
ctEtherDuplexAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctEtherDuplexAdminStatus.setStatus(_A)
class _CtEtherDuplexOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_CtEtherDuplexOperStatus_Type.__name__=_B
_CtEtherDuplexOperStatus_Object=MibTableColumn
ctEtherDuplexOperStatus=_CtEtherDuplexOperStatus_Object((1,3,6,1,4,1,52,4,1,2,4,2,3,1,1,6),_CtEtherDuplexOperStatus_Type())
ctEtherDuplexOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctEtherDuplexOperStatus.setStatus(_A)
mibBuilder.exportSymbols('CTRON-ETHERNET-PARAMETERS-MIB',**{'ctAutoNegCtl':ctAutoNegCtl,'ctAutoNegCtlTable':ctAutoNegCtlTable,'ctAutoNegCtlEntry':ctAutoNegCtlEntry,'ctAutoNegAdminStatus':ctAutoNegAdminStatus,'ctAutoNegRemoteSignalling':ctAutoNegRemoteSignalling,'ctAutoNegAutoConfig':ctAutoNegAutoConfig,'ctAutoNegLocalTechnologyAbility':ctAutoNegLocalTechnologyAbility,'ctAutoNegAdvertisedTechnologyAbility':ctAutoNegAdvertisedTechnologyAbility,'ctAutoNegReceivedTechnologyAbility':ctAutoNegReceivedTechnologyAbility,'ctFlowControl':ctFlowControl,'ctFlowCtlTable':ctFlowCtlTable,'ctFlowCtlEntry':ctFlowCtlEntry,'ctFlowCtlHalfDuplexAdminStatus':ctFlowCtlHalfDuplexAdminStatus,'ctFlowCtlHalfDuplexOperStatus':ctFlowCtlHalfDuplexOperStatus,'ctEtherSupportedPauseModes':ctEtherSupportedPauseModes,'ctFlowCtlPauseAdminStatus':ctFlowCtlPauseAdminStatus,'ctFlowCtlPauseOperStatus':ctFlowCtlPauseOperStatus,'ctFlowCtlPauseTimer':ctFlowCtlPauseTimer,'ctFlowCtlRxPauseFrames':ctFlowCtlRxPauseFrames,'ctFlowCtlTxPauseFrames':ctFlowCtlTxPauseFrames,'ctEtherManualConfig':ctEtherManualConfig,'ctEtherManualConfigTable':ctEtherManualConfigTable,'ctEtherManualConfigEntry':ctEtherManualConfigEntry,'ctEtherSupportedSpeed':ctEtherSupportedSpeed,'ctEtherSpeedAdminStatus':ctEtherSpeedAdminStatus,'ctEtherSpeedOperStatus':ctEtherSpeedOperStatus,'ctEtherSupportedDuplex':ctEtherSupportedDuplex,'ctEtherDuplexAdminStatus':ctEtherDuplexAdminStatus,'ctEtherDuplexOperStatus':ctEtherDuplexOperStatus})