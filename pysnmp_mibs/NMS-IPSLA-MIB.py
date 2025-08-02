_F='nmsIpslaEchoTargetPort'
_E='nmsIpslaJobEntryIndex'
_D='NMS-IPSLA-MIB'
_C='mandatory'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmsMgmt,=mibBuilder.importSymbols('NMS-SMI','nmsMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nmsIpslaMIB=ModuleIdentity((1,3,6,1,4,1,3320,9,102))
_NmsIpslaJitterObjects_ObjectIdentity=ObjectIdentity
nmsIpslaJitterObjects=_NmsIpslaJitterObjects_ObjectIdentity((1,3,6,1,4,1,3320,9,102,1))
_IpslaJitterTable_Object=MibTable
ipslaJitterTable=_IpslaJitterTable_Object((1,3,6,1,4,1,3320,9,102,1,1))
if mibBuilder.loadTexts:ipslaJitterTable.setStatus(_C)
_NmsIpslaJitterEntry_Object=MibTableRow
nmsIpslaJitterEntry=_NmsIpslaJitterEntry_Object((1,3,6,1,4,1,3320,9,102,1,1,1))
nmsIpslaJitterEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:nmsIpslaJitterEntry.setStatus(_C)
_NmsIpslaJobEntryIndex_Type=Integer32
_NmsIpslaJobEntryIndex_Object=MibTableColumn
nmsIpslaJobEntryIndex=_NmsIpslaJobEntryIndex_Object((1,3,6,1,4,1,3320,9,102,1,1,1,1),_NmsIpslaJobEntryIndex_Type())
nmsIpslaJobEntryIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaJobEntryIndex.setStatus(_C)
_NmsIpslaJobSuccesses_Type=Integer32
_NmsIpslaJobSuccesses_Object=MibTableColumn
nmsIpslaJobSuccesses=_NmsIpslaJobSuccesses_Object((1,3,6,1,4,1,3320,9,102,1,1,1,2),_NmsIpslaJobSuccesses_Type())
nmsIpslaJobSuccesses.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaJobSuccesses.setStatus(_B)
_NmsIpslaJobFailures_Type=Integer32
_NmsIpslaJobFailures_Object=MibTableColumn
nmsIpslaJobFailures=_NmsIpslaJobFailures_Object((1,3,6,1,4,1,3320,9,102,1,1,1,3),_NmsIpslaJobFailures_Type())
nmsIpslaJobFailures.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaJobFailures.setStatus(_B)
_NmsIpslaJitterSamples_Type=Integer32
_NmsIpslaJitterSamples_Object=MibTableColumn
nmsIpslaJitterSamples=_NmsIpslaJitterSamples_Object((1,3,6,1,4,1,3320,9,102,1,1,1,4),_NmsIpslaJitterSamples_Type())
nmsIpslaJitterSamples.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaJitterSamples.setStatus(_B)
_NmsIpslaJitterSrc2DstMin_Type=Integer32
_NmsIpslaJitterSrc2DstMin_Object=MibTableColumn
nmsIpslaJitterSrc2DstMin=_NmsIpslaJitterSrc2DstMin_Object((1,3,6,1,4,1,3320,9,102,1,1,1,5),_NmsIpslaJitterSrc2DstMin_Type())
nmsIpslaJitterSrc2DstMin.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaJitterSrc2DstMin.setStatus(_B)
_NmsIpslaJitterSrc2DstMax_Type=Integer32
_NmsIpslaJitterSrc2DstMax_Object=MibTableColumn
nmsIpslaJitterSrc2DstMax=_NmsIpslaJitterSrc2DstMax_Object((1,3,6,1,4,1,3320,9,102,1,1,1,6),_NmsIpslaJitterSrc2DstMax_Type())
nmsIpslaJitterSrc2DstMax.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaJitterSrc2DstMax.setStatus(_B)
_NmsIpslaJitterSrc2DstAvg_Type=Integer32
_NmsIpslaJitterSrc2DstAvg_Object=MibTableColumn
nmsIpslaJitterSrc2DstAvg=_NmsIpslaJitterSrc2DstAvg_Object((1,3,6,1,4,1,3320,9,102,1,1,1,7),_NmsIpslaJitterSrc2DstAvg_Type())
nmsIpslaJitterSrc2DstAvg.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaJitterSrc2DstAvg.setStatus(_B)
_NmsIpslaJitterDst2SrcMin_Type=Integer32
_NmsIpslaJitterDst2SrcMin_Object=MibTableColumn
nmsIpslaJitterDst2SrcMin=_NmsIpslaJitterDst2SrcMin_Object((1,3,6,1,4,1,3320,9,102,1,1,1,8),_NmsIpslaJitterDst2SrcMin_Type())
nmsIpslaJitterDst2SrcMin.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaJitterDst2SrcMin.setStatus(_B)
_NmsIpslaJitterDst2SrcMax_Type=Integer32
_NmsIpslaJitterDst2SrcMax_Object=MibTableColumn
nmsIpslaJitterDst2SrcMax=_NmsIpslaJitterDst2SrcMax_Object((1,3,6,1,4,1,3320,9,102,1,1,1,9),_NmsIpslaJitterDst2SrcMax_Type())
nmsIpslaJitterDst2SrcMax.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaJitterDst2SrcMax.setStatus(_B)
_NmsIpslaJitterDst2SrcAvg_Type=Integer32
_NmsIpslaJitterDst2SrcAvg_Object=MibTableColumn
nmsIpslaJitterDst2SrcAvg=_NmsIpslaJitterDst2SrcAvg_Object((1,3,6,1,4,1,3320,9,102,1,1,1,10),_NmsIpslaJitterDst2SrcAvg_Type())
nmsIpslaJitterDst2SrcAvg.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaJitterDst2SrcAvg.setStatus(_B)
_NmsIpslaJitterRttMin_Type=Integer32
_NmsIpslaJitterRttMin_Object=MibTableColumn
nmsIpslaJitterRttMin=_NmsIpslaJitterRttMin_Object((1,3,6,1,4,1,3320,9,102,1,1,1,11),_NmsIpslaJitterRttMin_Type())
nmsIpslaJitterRttMin.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaJitterRttMin.setStatus(_B)
_NmsIpslaJitterRttMax_Type=Integer32
_NmsIpslaJitterRttMax_Object=MibTableColumn
nmsIpslaJitterRttMax=_NmsIpslaJitterRttMax_Object((1,3,6,1,4,1,3320,9,102,1,1,1,12),_NmsIpslaJitterRttMax_Type())
nmsIpslaJitterRttMax.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaJitterRttMax.setStatus(_B)
_NmsIpslaJitterRttAvg_Type=Integer32
_NmsIpslaJitterRttAvg_Object=MibTableColumn
nmsIpslaJitterRttAvg=_NmsIpslaJitterRttAvg_Object((1,3,6,1,4,1,3320,9,102,1,1,1,13),_NmsIpslaJitterRttAvg_Type())
nmsIpslaJitterRttAvg.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaJitterRttAvg.setStatus(_B)
_NmsIpslaEchoObjects_ObjectIdentity=ObjectIdentity
nmsIpslaEchoObjects=_NmsIpslaEchoObjects_ObjectIdentity((1,3,6,1,4,1,3320,9,102,2))
_IpslaEchoTable_Object=MibTable
ipslaEchoTable=_IpslaEchoTable_Object((1,3,6,1,4,1,3320,9,102,2,1))
if mibBuilder.loadTexts:ipslaEchoTable.setStatus(_C)
_NmsIpslaEchoEntry_Object=MibTableRow
nmsIpslaEchoEntry=_NmsIpslaEchoEntry_Object((1,3,6,1,4,1,3320,9,102,2,1,1))
nmsIpslaEchoEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:nmsIpslaEchoEntry.setStatus(_C)
_NmsIpslaEchoTargetPort_Type=Integer32
_NmsIpslaEchoTargetPort_Object=MibTableColumn
nmsIpslaEchoTargetPort=_NmsIpslaEchoTargetPort_Object((1,3,6,1,4,1,3320,9,102,2,1,1,1),_NmsIpslaEchoTargetPort_Type())
nmsIpslaEchoTargetPort.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaEchoTargetPort.setStatus(_C)
_NmsIpslaEchoSourcePort_Type=Integer32
_NmsIpslaEchoSourcePort_Object=MibTableColumn
nmsIpslaEchoSourcePort=_NmsIpslaEchoSourcePort_Object((1,3,6,1,4,1,3320,9,102,2,1,1,2),_NmsIpslaEchoSourcePort_Type())
nmsIpslaEchoSourcePort.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaEchoSourcePort.setStatus(_B)
_NmsIpslaEchoRtt_Type=Integer32
_NmsIpslaEchoRtt_Object=MibTableColumn
nmsIpslaEchoRtt=_NmsIpslaEchoRtt_Object((1,3,6,1,4,1,3320,9,102,2,1,1,3),_NmsIpslaEchoRtt_Type())
nmsIpslaEchoRtt.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaEchoRtt.setStatus(_B)
_NmsIpslaEchoProbeSent_Type=Integer32
_NmsIpslaEchoProbeSent_Object=MibTableColumn
nmsIpslaEchoProbeSent=_NmsIpslaEchoProbeSent_Object((1,3,6,1,4,1,3320,9,102,2,1,1,4),_NmsIpslaEchoProbeSent_Type())
nmsIpslaEchoProbeSent.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaEchoProbeSent.setStatus(_B)
_NmsIpslaEchoProbeCompletion_Type=Integer32
_NmsIpslaEchoProbeCompletion_Object=MibTableColumn
nmsIpslaEchoProbeCompletion=_NmsIpslaEchoProbeCompletion_Object((1,3,6,1,4,1,3320,9,102,2,1,1,5),_NmsIpslaEchoProbeCompletion_Type())
nmsIpslaEchoProbeCompletion.setMaxAccess(_A)
if mibBuilder.loadTexts:nmsIpslaEchoProbeCompletion.setStatus(_B)
mibBuilder.exportSymbols(_D,**{'nmsIpslaMIB':nmsIpslaMIB,'nmsIpslaJitterObjects':nmsIpslaJitterObjects,'ipslaJitterTable':ipslaJitterTable,'nmsIpslaJitterEntry':nmsIpslaJitterEntry,_E:nmsIpslaJobEntryIndex,'nmsIpslaJobSuccesses':nmsIpslaJobSuccesses,'nmsIpslaJobFailures':nmsIpslaJobFailures,'nmsIpslaJitterSamples':nmsIpslaJitterSamples,'nmsIpslaJitterSrc2DstMin':nmsIpslaJitterSrc2DstMin,'nmsIpslaJitterSrc2DstMax':nmsIpslaJitterSrc2DstMax,'nmsIpslaJitterSrc2DstAvg':nmsIpslaJitterSrc2DstAvg,'nmsIpslaJitterDst2SrcMin':nmsIpslaJitterDst2SrcMin,'nmsIpslaJitterDst2SrcMax':nmsIpslaJitterDst2SrcMax,'nmsIpslaJitterDst2SrcAvg':nmsIpslaJitterDst2SrcAvg,'nmsIpslaJitterRttMin':nmsIpslaJitterRttMin,'nmsIpslaJitterRttMax':nmsIpslaJitterRttMax,'nmsIpslaJitterRttAvg':nmsIpslaJitterRttAvg,'nmsIpslaEchoObjects':nmsIpslaEchoObjects,'ipslaEchoTable':ipslaEchoTable,'nmsIpslaEchoEntry':nmsIpslaEchoEntry,_F:nmsIpslaEchoTargetPort,'nmsIpslaEchoSourcePort':nmsIpslaEchoSourcePort,'nmsIpslaEchoRtt':nmsIpslaEchoRtt,'nmsIpslaEchoProbeSent':nmsIpslaEchoProbeSent,'nmsIpslaEchoProbeCompletion':nmsIpslaEchoProbeCompletion})