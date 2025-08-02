_R='read-only'
_Q='fsTacMcastChannelSrcAddress'
_P='fsTacMcastChannelGrpAddress'
_O='fsTacMcastChannelAddressType'
_N='fsTacMcastPrfFilterSrcEndAddr'
_M='fsTacMcastPrfFilterSrcStartAddr'
_L='fsTacMcastPrfFilterGrpEndAddr'
_K='fsTacMcastPrfFilterGrpStartAddr'
_J='DisplayString'
_I='fsTacMcastProfileAddrType'
_H='fsTacMcastProfileId'
_G='Unsigned32'
_F='Integer32'
_E='InetAddress'
_D='not-accessible'
_C='read-write'
_B='SUPERMICRO-TAC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_E,'InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention')
fstac=ModuleIdentity((1,3,6,1,4,1,10876,101,2,8))
if mibBuilder.loadTexts:fstac.setRevisions(('2012-09-05 00:00',))
_FsTacScalars_ObjectIdentity=ObjectIdentity
fsTacScalars=_FsTacScalars_ObjectIdentity((1,3,6,1,4,1,10876,101,2,8,1))
class _FsTacMcastChannelDefaultBandwidth_Type(Unsigned32):defaultValue=2000
_FsTacMcastChannelDefaultBandwidth_Type.__name__=_G
_FsTacMcastChannelDefaultBandwidth_Object=MibScalar
fsTacMcastChannelDefaultBandwidth=_FsTacMcastChannelDefaultBandwidth_Object((1,3,6,1,4,1,10876,101,2,8,1,1),_FsTacMcastChannelDefaultBandwidth_Type())
fsTacMcastChannelDefaultBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTacMcastChannelDefaultBandwidth.setStatus(_A)
_FsTacTraceOption_Type=Unsigned32
_FsTacTraceOption_Object=MibScalar
fsTacTraceOption=_FsTacTraceOption_Object((1,3,6,1,4,1,10876,101,2,8,1,2),_FsTacTraceOption_Type())
fsTacTraceOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTacTraceOption.setStatus(_A)
class _FsTacStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsTacStatus_Type.__name__=_F
_FsTacStatus_Object=MibScalar
fsTacStatus=_FsTacStatus_Object((1,3,6,1,4,1,10876,101,2,8,1,3),_FsTacStatus_Type())
fsTacStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTacStatus.setStatus(_A)
_FsTacProfile_ObjectIdentity=ObjectIdentity
fsTacProfile=_FsTacProfile_ObjectIdentity((1,3,6,1,4,1,10876,101,2,8,2))
_FsTacMcastProfileTable_Object=MibTable
fsTacMcastProfileTable=_FsTacMcastProfileTable_Object((1,3,6,1,4,1,10876,101,2,8,2,1))
if mibBuilder.loadTexts:fsTacMcastProfileTable.setStatus(_A)
_FsTacMcastProfileEntry_Object=MibTableRow
fsTacMcastProfileEntry=_FsTacMcastProfileEntry_Object((1,3,6,1,4,1,10876,101,2,8,2,1,1))
fsTacMcastProfileEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:fsTacMcastProfileEntry.setStatus(_A)
class _FsTacMcastProfileId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_FsTacMcastProfileId_Type.__name__=_G
_FsTacMcastProfileId_Object=MibTableColumn
fsTacMcastProfileId=_FsTacMcastProfileId_Object((1,3,6,1,4,1,10876,101,2,8,2,1,1,1),_FsTacMcastProfileId_Type())
fsTacMcastProfileId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacMcastProfileId.setStatus(_A)
_FsTacMcastProfileAddrType_Type=InetAddressType
_FsTacMcastProfileAddrType_Object=MibTableColumn
fsTacMcastProfileAddrType=_FsTacMcastProfileAddrType_Object((1,3,6,1,4,1,10876,101,2,8,2,1,1,2),_FsTacMcastProfileAddrType_Type())
fsTacMcastProfileAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacMcastProfileAddrType.setStatus(_A)
class _FsTacMcastProfileAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_FsTacMcastProfileAction_Type.__name__=_F
_FsTacMcastProfileAction_Object=MibTableColumn
fsTacMcastProfileAction=_FsTacMcastProfileAction_Object((1,3,6,1,4,1,10876,101,2,8,2,1,1,3),_FsTacMcastProfileAction_Type())
fsTacMcastProfileAction.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTacMcastProfileAction.setStatus(_A)
class _FsTacMcastProfileDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FsTacMcastProfileDescription_Type.__name__=_J
_FsTacMcastProfileDescription_Object=MibTableColumn
fsTacMcastProfileDescription=_FsTacMcastProfileDescription_Object((1,3,6,1,4,1,10876,101,2,8,2,1,1,4),_FsTacMcastProfileDescription_Type())
fsTacMcastProfileDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTacMcastProfileDescription.setStatus(_A)
_FsTacMcastProfileStatus_Type=RowStatus
_FsTacMcastProfileStatus_Object=MibTableColumn
fsTacMcastProfileStatus=_FsTacMcastProfileStatus_Object((1,3,6,1,4,1,10876,101,2,8,2,1,1,5),_FsTacMcastProfileStatus_Type())
fsTacMcastProfileStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTacMcastProfileStatus.setStatus(_A)
_FsTacMcastPrfFilterTable_Object=MibTable
fsTacMcastPrfFilterTable=_FsTacMcastPrfFilterTable_Object((1,3,6,1,4,1,10876,101,2,8,2,2))
if mibBuilder.loadTexts:fsTacMcastPrfFilterTable.setStatus(_A)
_FsTacMcastPrfFilterEntry_Object=MibTableRow
fsTacMcastPrfFilterEntry=_FsTacMcastPrfFilterEntry_Object((1,3,6,1,4,1,10876,101,2,8,2,2,1))
fsTacMcastPrfFilterEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:fsTacMcastPrfFilterEntry.setStatus(_A)
class _FsTacMcastPrfFilterGrpStartAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_FsTacMcastPrfFilterGrpStartAddr_Type.__name__=_E
_FsTacMcastPrfFilterGrpStartAddr_Object=MibTableColumn
fsTacMcastPrfFilterGrpStartAddr=_FsTacMcastPrfFilterGrpStartAddr_Object((1,3,6,1,4,1,10876,101,2,8,2,2,1,1),_FsTacMcastPrfFilterGrpStartAddr_Type())
fsTacMcastPrfFilterGrpStartAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacMcastPrfFilterGrpStartAddr.setStatus(_A)
class _FsTacMcastPrfFilterGrpEndAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_FsTacMcastPrfFilterGrpEndAddr_Type.__name__=_E
_FsTacMcastPrfFilterGrpEndAddr_Object=MibTableColumn
fsTacMcastPrfFilterGrpEndAddr=_FsTacMcastPrfFilterGrpEndAddr_Object((1,3,6,1,4,1,10876,101,2,8,2,2,1,2),_FsTacMcastPrfFilterGrpEndAddr_Type())
fsTacMcastPrfFilterGrpEndAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacMcastPrfFilterGrpEndAddr.setStatus(_A)
class _FsTacMcastPrfFilterSrcStartAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_FsTacMcastPrfFilterSrcStartAddr_Type.__name__=_E
_FsTacMcastPrfFilterSrcStartAddr_Object=MibTableColumn
fsTacMcastPrfFilterSrcStartAddr=_FsTacMcastPrfFilterSrcStartAddr_Object((1,3,6,1,4,1,10876,101,2,8,2,2,1,3),_FsTacMcastPrfFilterSrcStartAddr_Type())
fsTacMcastPrfFilterSrcStartAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacMcastPrfFilterSrcStartAddr.setStatus(_A)
class _FsTacMcastPrfFilterSrcEndAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_FsTacMcastPrfFilterSrcEndAddr_Type.__name__=_E
_FsTacMcastPrfFilterSrcEndAddr_Object=MibTableColumn
fsTacMcastPrfFilterSrcEndAddr=_FsTacMcastPrfFilterSrcEndAddr_Object((1,3,6,1,4,1,10876,101,2,8,2,2,1,4),_FsTacMcastPrfFilterSrcEndAddr_Type())
fsTacMcastPrfFilterSrcEndAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacMcastPrfFilterSrcEndAddr.setStatus(_A)
class _FsTacMcastPrfFilterMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('include',1),('exclude',2),('any',3)))
_FsTacMcastPrfFilterMode_Type.__name__=_F
_FsTacMcastPrfFilterMode_Object=MibTableColumn
fsTacMcastPrfFilterMode=_FsTacMcastPrfFilterMode_Object((1,3,6,1,4,1,10876,101,2,8,2,2,1,5),_FsTacMcastPrfFilterMode_Type())
fsTacMcastPrfFilterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTacMcastPrfFilterMode.setStatus(_A)
_FsTacMcastPrfFilterStatus_Type=RowStatus
_FsTacMcastPrfFilterStatus_Object=MibTableColumn
fsTacMcastPrfFilterStatus=_FsTacMcastPrfFilterStatus_Object((1,3,6,1,4,1,10876,101,2,8,2,2,1,6),_FsTacMcastPrfFilterStatus_Type())
fsTacMcastPrfFilterStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTacMcastPrfFilterStatus.setStatus(_A)
_FsTacChannels_ObjectIdentity=ObjectIdentity
fsTacChannels=_FsTacChannels_ObjectIdentity((1,3,6,1,4,1,10876,101,2,8,3))
_FsTacMcastChannelTable_Object=MibTable
fsTacMcastChannelTable=_FsTacMcastChannelTable_Object((1,3,6,1,4,1,10876,101,2,8,3,1))
if mibBuilder.loadTexts:fsTacMcastChannelTable.setStatus(_A)
_FsTacMcastChannelEntry_Object=MibTableRow
fsTacMcastChannelEntry=_FsTacMcastChannelEntry_Object((1,3,6,1,4,1,10876,101,2,8,3,1,1))
fsTacMcastChannelEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:fsTacMcastChannelEntry.setStatus(_A)
_FsTacMcastChannelAddressType_Type=InetAddressType
_FsTacMcastChannelAddressType_Object=MibTableColumn
fsTacMcastChannelAddressType=_FsTacMcastChannelAddressType_Object((1,3,6,1,4,1,10876,101,2,8,3,1,1,1),_FsTacMcastChannelAddressType_Type())
fsTacMcastChannelAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacMcastChannelAddressType.setStatus(_A)
class _FsTacMcastChannelGrpAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_FsTacMcastChannelGrpAddress_Type.__name__=_E
_FsTacMcastChannelGrpAddress_Object=MibTableColumn
fsTacMcastChannelGrpAddress=_FsTacMcastChannelGrpAddress_Object((1,3,6,1,4,1,10876,101,2,8,3,1,1,2),_FsTacMcastChannelGrpAddress_Type())
fsTacMcastChannelGrpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacMcastChannelGrpAddress.setStatus(_A)
class _FsTacMcastChannelSrcAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_FsTacMcastChannelSrcAddress_Type.__name__=_E
_FsTacMcastChannelSrcAddress_Object=MibTableColumn
fsTacMcastChannelSrcAddress=_FsTacMcastChannelSrcAddress_Object((1,3,6,1,4,1,10876,101,2,8,3,1,1,3),_FsTacMcastChannelSrcAddress_Type())
fsTacMcastChannelSrcAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsTacMcastChannelSrcAddress.setStatus(_A)
class _FsTacMcastChannelBandWidth_Type(Unsigned32):defaultValue=2000
_FsTacMcastChannelBandWidth_Type.__name__=_G
_FsTacMcastChannelBandWidth_Object=MibTableColumn
fsTacMcastChannelBandWidth=_FsTacMcastChannelBandWidth_Object((1,3,6,1,4,1,10876,101,2,8,3,1,1,4),_FsTacMcastChannelBandWidth_Type())
fsTacMcastChannelBandWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTacMcastChannelBandWidth.setStatus(_A)
_FsTacMcastChannelRowStatus_Type=RowStatus
_FsTacMcastChannelRowStatus_Object=MibTableColumn
fsTacMcastChannelRowStatus=_FsTacMcastChannelRowStatus_Object((1,3,6,1,4,1,10876,101,2,8,3,1,1,5),_FsTacMcastChannelRowStatus_Type())
fsTacMcastChannelRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTacMcastChannelRowStatus.setStatus(_A)
_FsTacStatistics_ObjectIdentity=ObjectIdentity
fsTacStatistics=_FsTacStatistics_ObjectIdentity((1,3,6,1,4,1,10876,101,2,8,4))
_FsTacMcastPrfStatsTable_Object=MibTable
fsTacMcastPrfStatsTable=_FsTacMcastPrfStatsTable_Object((1,3,6,1,4,1,10876,101,2,8,4,1))
if mibBuilder.loadTexts:fsTacMcastPrfStatsTable.setStatus(_A)
_FsTacMcastPrfStatsEntry_Object=MibTableRow
fsTacMcastPrfStatsEntry=_FsTacMcastPrfStatsEntry_Object((1,3,6,1,4,1,10876,101,2,8,4,1,1))
fsTacMcastPrfStatsEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:fsTacMcastPrfStatsEntry.setStatus(_A)
_FsTacMcastPrfStatsPortRefCnt_Type=Unsigned32
_FsTacMcastPrfStatsPortRefCnt_Object=MibTableColumn
fsTacMcastPrfStatsPortRefCnt=_FsTacMcastPrfStatsPortRefCnt_Object((1,3,6,1,4,1,10876,101,2,8,4,1,1,1),_FsTacMcastPrfStatsPortRefCnt_Type())
fsTacMcastPrfStatsPortRefCnt.setMaxAccess(_R)
if mibBuilder.loadTexts:fsTacMcastPrfStatsPortRefCnt.setStatus(_A)
_FsTacMcastPrfStatsVlanRefCnt_Type=Unsigned32
_FsTacMcastPrfStatsVlanRefCnt_Object=MibTableColumn
fsTacMcastPrfStatsVlanRefCnt=_FsTacMcastPrfStatsVlanRefCnt_Object((1,3,6,1,4,1,10876,101,2,8,4,1,1,2),_FsTacMcastPrfStatsVlanRefCnt_Type())
fsTacMcastPrfStatsVlanRefCnt.setMaxAccess(_R)
if mibBuilder.loadTexts:fsTacMcastPrfStatsVlanRefCnt.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fstac':fstac,'fsTacScalars':fsTacScalars,'fsTacMcastChannelDefaultBandwidth':fsTacMcastChannelDefaultBandwidth,'fsTacTraceOption':fsTacTraceOption,'fsTacStatus':fsTacStatus,'fsTacProfile':fsTacProfile,'fsTacMcastProfileTable':fsTacMcastProfileTable,'fsTacMcastProfileEntry':fsTacMcastProfileEntry,_H:fsTacMcastProfileId,_I:fsTacMcastProfileAddrType,'fsTacMcastProfileAction':fsTacMcastProfileAction,'fsTacMcastProfileDescription':fsTacMcastProfileDescription,'fsTacMcastProfileStatus':fsTacMcastProfileStatus,'fsTacMcastPrfFilterTable':fsTacMcastPrfFilterTable,'fsTacMcastPrfFilterEntry':fsTacMcastPrfFilterEntry,_K:fsTacMcastPrfFilterGrpStartAddr,_L:fsTacMcastPrfFilterGrpEndAddr,_M:fsTacMcastPrfFilterSrcStartAddr,_N:fsTacMcastPrfFilterSrcEndAddr,'fsTacMcastPrfFilterMode':fsTacMcastPrfFilterMode,'fsTacMcastPrfFilterStatus':fsTacMcastPrfFilterStatus,'fsTacChannels':fsTacChannels,'fsTacMcastChannelTable':fsTacMcastChannelTable,'fsTacMcastChannelEntry':fsTacMcastChannelEntry,_O:fsTacMcastChannelAddressType,_P:fsTacMcastChannelGrpAddress,_Q:fsTacMcastChannelSrcAddress,'fsTacMcastChannelBandWidth':fsTacMcastChannelBandWidth,'fsTacMcastChannelRowStatus':fsTacMcastChannelRowStatus,'fsTacStatistics':fsTacStatistics,'fsTacMcastPrfStatsTable':fsTacMcastPrfStatsTable,'fsTacMcastPrfStatsEntry':fsTacMcastPrfStatsEntry,'fsTacMcastPrfStatsPortRefCnt':fsTacMcastPrfStatsPortRefCnt,'fsTacMcastPrfStatsVlanRefCnt':fsTacMcastPrfStatsVlanRefCnt})