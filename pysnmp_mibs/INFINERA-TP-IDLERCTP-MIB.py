_Q='idlerCtpGroup'
_P='pmHistStatsEnable'
_O='channelPower'
_N='channelFrequency'
_M='channelFrequencyOffset'
_L='targetOpt'
_K='laserStatus'
_J='sbsTone'
_I='sbsFrequencyWidth'
_H='sbsAmplitude'
_G='sbsMode'
_F='read-only'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='INFINERA-TP-IDLERCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatArbitraryPrecision,InfnLaserStatus,InfnPmHistStatsControl,InfnSBSMode=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','InfnLaserStatus','InfnPmHistStatsControl','InfnSBSMode')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
idlerCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,85))
if mibBuilder.loadTexts:idlerCtpMIB.setRevisions(('2017-06-28 00:00',))
_IdlerCtpTable_Object=MibTable
idlerCtpTable=_IdlerCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,85,1))
if mibBuilder.loadTexts:idlerCtpTable.setStatus(_A)
_IdlerCtpEntry_Object=MibTableRow
idlerCtpEntry=_IdlerCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,85,1,1))
idlerCtpEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:idlerCtpEntry.setStatus(_A)
_MoID_Type=DisplayString
_MoID_Object=MibTableColumn
moID=_MoID_Object((1,3,6,1,4,1,21296,2,2,2,2,85,1,1,1),_MoID_Type())
moID.setMaxAccess('read-create')
if mibBuilder.loadTexts:moID.setStatus(_A)
_SbsMode_Type=InfnSBSMode
_SbsMode_Object=MibTableColumn
sbsMode=_SbsMode_Object((1,3,6,1,4,1,21296,2,2,2,2,85,1,1,2),_SbsMode_Type())
sbsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sbsMode.setStatus(_A)
_SbsAmplitude_Type=FloatArbitraryPrecision
_SbsAmplitude_Object=MibTableColumn
sbsAmplitude=_SbsAmplitude_Object((1,3,6,1,4,1,21296,2,2,2,2,85,1,1,3),_SbsAmplitude_Type())
sbsAmplitude.setMaxAccess(_C)
if mibBuilder.loadTexts:sbsAmplitude.setStatus(_A)
_SbsFrequencyWidth_Type=FloatArbitraryPrecision
_SbsFrequencyWidth_Object=MibTableColumn
sbsFrequencyWidth=_SbsFrequencyWidth_Object((1,3,6,1,4,1,21296,2,2,2,2,85,1,1,4),_SbsFrequencyWidth_Type())
sbsFrequencyWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:sbsFrequencyWidth.setStatus(_A)
_SbsTone_Type=FloatArbitraryPrecision
_SbsTone_Object=MibTableColumn
sbsTone=_SbsTone_Object((1,3,6,1,4,1,21296,2,2,2,2,85,1,1,5),_SbsTone_Type())
sbsTone.setMaxAccess(_F)
if mibBuilder.loadTexts:sbsTone.setStatus(_A)
_LaserStatus_Type=InfnLaserStatus
_LaserStatus_Object=MibTableColumn
laserStatus=_LaserStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,85,1,1,6),_LaserStatus_Type())
laserStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:laserStatus.setStatus(_A)
_TargetOpt_Type=FloatArbitraryPrecision
_TargetOpt_Object=MibTableColumn
targetOpt=_TargetOpt_Object((1,3,6,1,4,1,21296,2,2,2,2,85,1,1,7),_TargetOpt_Type())
targetOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:targetOpt.setStatus(_A)
_ChannelFrequencyOffset_Type=FloatArbitraryPrecision
_ChannelFrequencyOffset_Object=MibTableColumn
channelFrequencyOffset=_ChannelFrequencyOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,85,1,1,8),_ChannelFrequencyOffset_Type())
channelFrequencyOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:channelFrequencyOffset.setStatus(_A)
_ChannelFrequency_Type=FloatArbitraryPrecision
_ChannelFrequency_Object=MibTableColumn
channelFrequency=_ChannelFrequency_Object((1,3,6,1,4,1,21296,2,2,2,2,85,1,1,9),_ChannelFrequency_Type())
channelFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:channelFrequency.setStatus(_A)
_ChannelPower_Type=FloatArbitraryPrecision
_ChannelPower_Object=MibTableColumn
channelPower=_ChannelPower_Object((1,3,6,1,4,1,21296,2,2,2,2,85,1,1,10),_ChannelPower_Type())
channelPower.setMaxAccess(_C)
if mibBuilder.loadTexts:channelPower.setStatus(_A)
_PmHistStatsEnable_Type=InfnPmHistStatsControl
_PmHistStatsEnable_Object=MibTableColumn
pmHistStatsEnable=_PmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,85,1,1,11),_PmHistStatsEnable_Type())
pmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:pmHistStatsEnable.setStatus(_A)
_IdlerCtpConformance_ObjectIdentity=ObjectIdentity
idlerCtpConformance=_IdlerCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,85,3))
_IdlerCtpCompliances_ObjectIdentity=ObjectIdentity
idlerCtpCompliances=_IdlerCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,85,3,1))
_IdlerCtpGroups_ObjectIdentity=ObjectIdentity
idlerCtpGroups=_IdlerCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,85,3,2))
idlerCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,85,3,2,1))
idlerCtpGroup.setObjects(*((_B,'moID'),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:idlerCtpGroup.setStatus(_A)
idlerCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,85,3,1,1))
idlerCtpCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:idlerCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'idlerCtpMIB':idlerCtpMIB,'idlerCtpTable':idlerCtpTable,'idlerCtpEntry':idlerCtpEntry,'moID':moID,_G:sbsMode,_H:sbsAmplitude,_I:sbsFrequencyWidth,_J:sbsTone,_K:laserStatus,_L:targetOpt,_M:channelFrequencyOffset,_N:channelFrequency,_O:channelPower,_P:pmHistStatsEnable,'idlerCtpConformance':idlerCtpConformance,'idlerCtpCompliances':idlerCtpCompliances,'idlerCtpCompliance':idlerCtpCompliance,'idlerCtpGroups':idlerCtpGroups,_Q:idlerCtpGroup})