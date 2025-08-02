_T='qosIeee8021qSubstitutionGroupVer1'
_S='qosIeee8021qGroupVer1'
_R='qosDiffServGroupVer1'
_Q='qosInteropUseVoiceQoSForRtcpEnable'
_P='qosVlanIeee8021qSubstitutionFiltering'
_O='qosVlanIeee8021qSubstitutionUserPriority'
_N='qosVlanIeee8021qSubstitutionVlanID'
_M='qosVlanIeee8021qSubstitutionEnable'
_L='qosVbdDiffServ'
_K='qosT38FaxDiffServ'
_J='qosVoiceDiffServ'
_I='qosSignalingDiffServ'
_H='MxEnableState'
_G='enable'
_F='disable'
_E='Integer32'
_D='Unsigned32'
_C='MX-QOS-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qosMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,20))
if mibBuilder.loadTexts:qosMIB.setRevisions(('2010-11-02 00:00','2009-03-06 00:00','2005-09-26 00:00','2005-02-21 00:00','2004-06-17 00:00','2001-08-23 00:00'))
_QosMIBObjects_ObjectIdentity=ObjectIdentity
qosMIBObjects=_QosMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,20,1))
_QosDiffServ_ObjectIdentity=ObjectIdentity
qosDiffServ=_QosDiffServ_ObjectIdentity((1,3,6,1,4,1,4935,15,20,1,1))
class _QosSignalingDiffServ_Type(Unsigned32):defaultValue=184;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QosSignalingDiffServ_Type.__name__=_D
_QosSignalingDiffServ_Object=MibScalar
qosSignalingDiffServ=_QosSignalingDiffServ_Object((1,3,6,1,4,1,4935,15,20,1,1,1),_QosSignalingDiffServ_Type())
qosSignalingDiffServ.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSignalingDiffServ.setStatus(_A)
class _QosVoiceDiffServ_Type(Unsigned32):defaultValue=184;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QosVoiceDiffServ_Type.__name__=_D
_QosVoiceDiffServ_Object=MibScalar
qosVoiceDiffServ=_QosVoiceDiffServ_Object((1,3,6,1,4,1,4935,15,20,1,1,2),_QosVoiceDiffServ_Type())
qosVoiceDiffServ.setMaxAccess(_B)
if mibBuilder.loadTexts:qosVoiceDiffServ.setStatus(_A)
class _QosT38FaxDiffServ_Type(Unsigned32):defaultValue=184;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QosT38FaxDiffServ_Type.__name__=_D
_QosT38FaxDiffServ_Object=MibScalar
qosT38FaxDiffServ=_QosT38FaxDiffServ_Object((1,3,6,1,4,1,4935,15,20,1,1,3),_QosT38FaxDiffServ_Type())
qosT38FaxDiffServ.setMaxAccess(_B)
if mibBuilder.loadTexts:qosT38FaxDiffServ.setStatus(_A)
class _QosVbdDiffServ_Type(Unsigned32):defaultValue=184;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QosVbdDiffServ_Type.__name__=_D
_QosVbdDiffServ_Object=MibScalar
qosVbdDiffServ=_QosVbdDiffServ_Object((1,3,6,1,4,1,4935,15,20,1,1,4),_QosVbdDiffServ_Type())
qosVbdDiffServ.setMaxAccess(_B)
if mibBuilder.loadTexts:qosVbdDiffServ.setStatus(_A)
_QosIeee8021q_ObjectIdentity=ObjectIdentity
qosIeee8021q=_QosIeee8021q_ObjectIdentity((1,3,6,1,4,1,4935,15,20,1,2))
class _QosSignalingIeee8021qEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_QosSignalingIeee8021qEnable_Type.__name__=_E
_QosSignalingIeee8021qEnable_Object=MibScalar
qosSignalingIeee8021qEnable=_QosSignalingIeee8021qEnable_Object((1,3,6,1,4,1,4935,15,20,1,2,1),_QosSignalingIeee8021qEnable_Type())
qosSignalingIeee8021qEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSignalingIeee8021qEnable.setStatus(_A)
class _QosSignalingIeee8021qUserPriority_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosSignalingIeee8021qUserPriority_Type.__name__=_D
_QosSignalingIeee8021qUserPriority_Object=MibScalar
qosSignalingIeee8021qUserPriority=_QosSignalingIeee8021qUserPriority_Object((1,3,6,1,4,1,4935,15,20,1,2,2),_QosSignalingIeee8021qUserPriority_Type())
qosSignalingIeee8021qUserPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:qosSignalingIeee8021qUserPriority.setStatus(_A)
class _QosVoiceIeee8021qEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_QosVoiceIeee8021qEnable_Type.__name__=_E
_QosVoiceIeee8021qEnable_Object=MibScalar
qosVoiceIeee8021qEnable=_QosVoiceIeee8021qEnable_Object((1,3,6,1,4,1,4935,15,20,1,2,3),_QosVoiceIeee8021qEnable_Type())
qosVoiceIeee8021qEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:qosVoiceIeee8021qEnable.setStatus(_A)
class _QosVoiceIeee8021qUserPriority_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosVoiceIeee8021qUserPriority_Type.__name__=_D
_QosVoiceIeee8021qUserPriority_Object=MibScalar
qosVoiceIeee8021qUserPriority=_QosVoiceIeee8021qUserPriority_Object((1,3,6,1,4,1,4935,15,20,1,2,4),_QosVoiceIeee8021qUserPriority_Type())
qosVoiceIeee8021qUserPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:qosVoiceIeee8021qUserPriority.setStatus(_A)
class _QosT38FaxIeee8021qEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_QosT38FaxIeee8021qEnable_Type.__name__=_E
_QosT38FaxIeee8021qEnable_Object=MibScalar
qosT38FaxIeee8021qEnable=_QosT38FaxIeee8021qEnable_Object((1,3,6,1,4,1,4935,15,20,1,2,5),_QosT38FaxIeee8021qEnable_Type())
qosT38FaxIeee8021qEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:qosT38FaxIeee8021qEnable.setStatus(_A)
class _QosT38FaxIeee8021qUserPriority_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosT38FaxIeee8021qUserPriority_Type.__name__=_D
_QosT38FaxIeee8021qUserPriority_Object=MibScalar
qosT38FaxIeee8021qUserPriority=_QosT38FaxIeee8021qUserPriority_Object((1,3,6,1,4,1,4935,15,20,1,2,6),_QosT38FaxIeee8021qUserPriority_Type())
qosT38FaxIeee8021qUserPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:qosT38FaxIeee8021qUserPriority.setStatus(_A)
class _QosVbdIeee8021qEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_QosVbdIeee8021qEnable_Type.__name__=_E
_QosVbdIeee8021qEnable_Object=MibScalar
qosVbdIeee8021qEnable=_QosVbdIeee8021qEnable_Object((1,3,6,1,4,1,4935,15,20,1,2,7),_QosVbdIeee8021qEnable_Type())
qosVbdIeee8021qEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:qosVbdIeee8021qEnable.setStatus(_A)
class _QosVbdIeee8021qUserPriority_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosVbdIeee8021qUserPriority_Type.__name__=_D
_QosVbdIeee8021qUserPriority_Object=MibScalar
qosVbdIeee8021qUserPriority=_QosVbdIeee8021qUserPriority_Object((1,3,6,1,4,1,4935,15,20,1,2,8),_QosVbdIeee8021qUserPriority_Type())
qosVbdIeee8021qUserPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:qosVbdIeee8021qUserPriority.setStatus(_A)
_QosVlanIeee8021q_ObjectIdentity=ObjectIdentity
qosVlanIeee8021q=_QosVlanIeee8021q_ObjectIdentity((1,3,6,1,4,1,4935,15,20,1,2,15))
class _QosVlanIeee8021qTaggingEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_QosVlanIeee8021qTaggingEnable_Type.__name__=_E
_QosVlanIeee8021qTaggingEnable_Object=MibScalar
qosVlanIeee8021qTaggingEnable=_QosVlanIeee8021qTaggingEnable_Object((1,3,6,1,4,1,4935,15,20,1,2,15,1),_QosVlanIeee8021qTaggingEnable_Type())
qosVlanIeee8021qTaggingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:qosVlanIeee8021qTaggingEnable.setStatus(_A)
class _QosVlanIeee8021qVirtualLanID_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_QosVlanIeee8021qVirtualLanID_Type.__name__=_D
_QosVlanIeee8021qVirtualLanID_Object=MibScalar
qosVlanIeee8021qVirtualLanID=_QosVlanIeee8021qVirtualLanID_Object((1,3,6,1,4,1,4935,15,20,1,2,15,2),_QosVlanIeee8021qVirtualLanID_Type())
qosVlanIeee8021qVirtualLanID.setMaxAccess(_B)
if mibBuilder.loadTexts:qosVlanIeee8021qVirtualLanID.setStatus(_A)
class _QosVlanIeee8021qDefaultUserPriority_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosVlanIeee8021qDefaultUserPriority_Type.__name__=_D
_QosVlanIeee8021qDefaultUserPriority_Object=MibScalar
qosVlanIeee8021qDefaultUserPriority=_QosVlanIeee8021qDefaultUserPriority_Object((1,3,6,1,4,1,4935,15,20,1,2,15,3),_QosVlanIeee8021qDefaultUserPriority_Type())
qosVlanIeee8021qDefaultUserPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:qosVlanIeee8021qDefaultUserPriority.setStatus(_A)
_QosIeee8021qSubstitution_ObjectIdentity=ObjectIdentity
qosIeee8021qSubstitution=_QosIeee8021qSubstitution_ObjectIdentity((1,3,6,1,4,1,4935,15,20,1,10))
class _QosVlanIeee8021qSubstitutionEnable_Type(MxEnableState):defaultValue=0
_QosVlanIeee8021qSubstitutionEnable_Type.__name__=_H
_QosVlanIeee8021qSubstitutionEnable_Object=MibScalar
qosVlanIeee8021qSubstitutionEnable=_QosVlanIeee8021qSubstitutionEnable_Object((1,3,6,1,4,1,4935,15,20,1,10,10),_QosVlanIeee8021qSubstitutionEnable_Type())
qosVlanIeee8021qSubstitutionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:qosVlanIeee8021qSubstitutionEnable.setStatus(_A)
class _QosVlanIeee8021qSubstitutionVlanID_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_QosVlanIeee8021qSubstitutionVlanID_Type.__name__=_D
_QosVlanIeee8021qSubstitutionVlanID_Object=MibScalar
qosVlanIeee8021qSubstitutionVlanID=_QosVlanIeee8021qSubstitutionVlanID_Object((1,3,6,1,4,1,4935,15,20,1,10,20),_QosVlanIeee8021qSubstitutionVlanID_Type())
qosVlanIeee8021qSubstitutionVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:qosVlanIeee8021qSubstitutionVlanID.setStatus(_A)
class _QosVlanIeee8021qSubstitutionUserPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosVlanIeee8021qSubstitutionUserPriority_Type.__name__=_D
_QosVlanIeee8021qSubstitutionUserPriority_Object=MibScalar
qosVlanIeee8021qSubstitutionUserPriority=_QosVlanIeee8021qSubstitutionUserPriority_Object((1,3,6,1,4,1,4935,15,20,1,10,30),_QosVlanIeee8021qSubstitutionUserPriority_Type())
qosVlanIeee8021qSubstitutionUserPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:qosVlanIeee8021qSubstitutionUserPriority.setStatus(_A)
class _QosVlanIeee8021qSubstitutionFiltering_Type(MxEnableState):defaultValue=0
_QosVlanIeee8021qSubstitutionFiltering_Type.__name__=_H
_QosVlanIeee8021qSubstitutionFiltering_Object=MibScalar
qosVlanIeee8021qSubstitutionFiltering=_QosVlanIeee8021qSubstitutionFiltering_Object((1,3,6,1,4,1,4935,15,20,1,10,40),_QosVlanIeee8021qSubstitutionFiltering_Type())
qosVlanIeee8021qSubstitutionFiltering.setMaxAccess(_B)
if mibBuilder.loadTexts:qosVlanIeee8021qSubstitutionFiltering.setStatus(_A)
_QosInterop_ObjectIdentity=ObjectIdentity
qosInterop=_QosInterop_ObjectIdentity((1,3,6,1,4,1,4935,15,20,1,20))
class _QosInteropUseVoiceQoSForRtcpEnable_Type(MxEnableState):defaultValue=0
_QosInteropUseVoiceQoSForRtcpEnable_Type.__name__=_H
_QosInteropUseVoiceQoSForRtcpEnable_Object=MibScalar
qosInteropUseVoiceQoSForRtcpEnable=_QosInteropUseVoiceQoSForRtcpEnable_Object((1,3,6,1,4,1,4935,15,20,1,20,10),_QosInteropUseVoiceQoSForRtcpEnable_Type())
qosInteropUseVoiceQoSForRtcpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInteropUseVoiceQoSForRtcpEnable.setStatus(_A)
_QosConformance_ObjectIdentity=ObjectIdentity
qosConformance=_QosConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,20,2))
_QosCompliances_ObjectIdentity=ObjectIdentity
qosCompliances=_QosCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,20,2,1))
_QosGroups_ObjectIdentity=ObjectIdentity
qosGroups=_QosGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,20,2,2))
qosDiffServGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,20,2,2,1))
qosDiffServGroupVer1.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:qosDiffServGroupVer1.setStatus(_A)
qosIeee8021qGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,20,2,2,2))
qosIeee8021qGroupVer1.setObjects(*((_C,_I),(_C,_J),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:qosIeee8021qGroupVer1.setStatus(_A)
qosIeee8021qSubstitutionGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,20,2,2,10))
qosIeee8021qSubstitutionGroupVer1.setObjects(*((_C,_M),(_C,_N),(_C,_O),(_C,_P)))
if mibBuilder.loadTexts:qosIeee8021qSubstitutionGroupVer1.setStatus(_A)
qosInteropGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,20,2,2,20))
qosInteropGroupVer1.setObjects((_C,_Q))
if mibBuilder.loadTexts:qosInteropGroupVer1.setStatus(_A)
qosAnalogComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,20,2,1,1))
qosAnalogComplVer1.setObjects(*((_C,_R),(_C,_S),(_C,_T)))
if mibBuilder.loadTexts:qosAnalogComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'qosMIB':qosMIB,'qosMIBObjects':qosMIBObjects,'qosDiffServ':qosDiffServ,_I:qosSignalingDiffServ,_J:qosVoiceDiffServ,_K:qosT38FaxDiffServ,_L:qosVbdDiffServ,'qosIeee8021q':qosIeee8021q,'qosSignalingIeee8021qEnable':qosSignalingIeee8021qEnable,'qosSignalingIeee8021qUserPriority':qosSignalingIeee8021qUserPriority,'qosVoiceIeee8021qEnable':qosVoiceIeee8021qEnable,'qosVoiceIeee8021qUserPriority':qosVoiceIeee8021qUserPriority,'qosT38FaxIeee8021qEnable':qosT38FaxIeee8021qEnable,'qosT38FaxIeee8021qUserPriority':qosT38FaxIeee8021qUserPriority,'qosVbdIeee8021qEnable':qosVbdIeee8021qEnable,'qosVbdIeee8021qUserPriority':qosVbdIeee8021qUserPriority,'qosVlanIeee8021q':qosVlanIeee8021q,'qosVlanIeee8021qTaggingEnable':qosVlanIeee8021qTaggingEnable,'qosVlanIeee8021qVirtualLanID':qosVlanIeee8021qVirtualLanID,'qosVlanIeee8021qDefaultUserPriority':qosVlanIeee8021qDefaultUserPriority,'qosIeee8021qSubstitution':qosIeee8021qSubstitution,_M:qosVlanIeee8021qSubstitutionEnable,_N:qosVlanIeee8021qSubstitutionVlanID,_O:qosVlanIeee8021qSubstitutionUserPriority,_P:qosVlanIeee8021qSubstitutionFiltering,'qosInterop':qosInterop,_Q:qosInteropUseVoiceQoSForRtcpEnable,'qosConformance':qosConformance,'qosCompliances':qosCompliances,'qosAnalogComplVer1':qosAnalogComplVer1,'qosGroups':qosGroups,_R:qosDiffServGroupVer1,_S:qosIeee8021qGroupVer1,_T:qosIeee8021qSubstitutionGroupVer1,'qosInteropGroupVer1':qosInteropGroupVer1})