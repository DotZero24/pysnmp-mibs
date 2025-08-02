_M='atNtpAssociationIndex'
_L='not-accessible'
_K='atNtpPeerIndex'
_J='RowStatus'
_I='DisplayString'
_H='Unsigned32'
_G='OctetString'
_F='millisecond'
_E='AT-NTP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress',_J,'TextualConvention','TruthValue')
atNtp=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,502))
if mibBuilder.loadTexts:atNtp.setRevisions(('2008-10-07 14:30',))
class _AtNtpPeerIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtNtpPeerIndexNext_Type.__name__=_C
_AtNtpPeerIndexNext_Object=MibScalar
atNtpPeerIndexNext=_AtNtpPeerIndexNext_Object((1,3,6,1,4,1,207,8,4,4,4,502,6),_AtNtpPeerIndexNext_Type())
atNtpPeerIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpPeerIndexNext.setStatus(_A)
_AtNtpPeerTable_Object=MibTable
atNtpPeerTable=_AtNtpPeerTable_Object((1,3,6,1,4,1,207,8,4,4,4,502,7))
if mibBuilder.loadTexts:atNtpPeerTable.setStatus(_A)
_AtNtpPeerEntry_Object=MibTableRow
atNtpPeerEntry=_AtNtpPeerEntry_Object((1,3,6,1,4,1,207,8,4,4,4,502,7,1))
atNtpPeerEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:atNtpPeerEntry.setStatus(_A)
class _AtNtpPeerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtNtpPeerIndex_Type.__name__=_C
_AtNtpPeerIndex_Object=MibTableColumn
atNtpPeerIndex=_AtNtpPeerIndex_Object((1,3,6,1,4,1,207,8,4,4,4,502,7,1,1),_AtNtpPeerIndex_Type())
atNtpPeerIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:atNtpPeerIndex.setStatus(_A)
class _AtNtpPeerNameAddr_Type(DisplayString):defaultValue=OctetString('0.0.0.0')
_AtNtpPeerNameAddr_Type.__name__=_I
_AtNtpPeerNameAddr_Object=MibTableColumn
atNtpPeerNameAddr=_AtNtpPeerNameAddr_Object((1,3,6,1,4,1,207,8,4,4,4,502,7,1,2),_AtNtpPeerNameAddr_Type())
atNtpPeerNameAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:atNtpPeerNameAddr.setStatus(_A)
class _AtNtpPeerMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('server',1),('peer',2)))
_AtNtpPeerMode_Type.__name__=_C
_AtNtpPeerMode_Object=MibTableColumn
atNtpPeerMode=_AtNtpPeerMode_Object((1,3,6,1,4,1,207,8,4,4,4,502,7,1,3),_AtNtpPeerMode_Type())
atNtpPeerMode.setMaxAccess(_D)
if mibBuilder.loadTexts:atNtpPeerMode.setStatus(_A)
class _AtNtpPeerPreference_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AtNtpPeerPreference_Type.__name__=_C
_AtNtpPeerPreference_Object=MibTableColumn
atNtpPeerPreference=_AtNtpPeerPreference_Object((1,3,6,1,4,1,207,8,4,4,4,502,7,1,4),_AtNtpPeerPreference_Type())
atNtpPeerPreference.setMaxAccess(_D)
if mibBuilder.loadTexts:atNtpPeerPreference.setStatus(_A)
class _AtNtpPeerVersion_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_AtNtpPeerVersion_Type.__name__=_C
_AtNtpPeerVersion_Object=MibTableColumn
atNtpPeerVersion=_AtNtpPeerVersion_Object((1,3,6,1,4,1,207,8,4,4,4,502,7,1,5),_AtNtpPeerVersion_Type())
atNtpPeerVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:atNtpPeerVersion.setStatus(_A)
class _AtNtpPeerKeyNumber_Type(Unsigned32):defaultValue=0
_AtNtpPeerKeyNumber_Type.__name__=_H
_AtNtpPeerKeyNumber_Object=MibTableColumn
atNtpPeerKeyNumber=_AtNtpPeerKeyNumber_Object((1,3,6,1,4,1,207,8,4,4,4,502,7,1,6),_AtNtpPeerKeyNumber_Type())
atNtpPeerKeyNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:atNtpPeerKeyNumber.setStatus(_A)
class _AtNtpPeerRowStatus_Type(RowStatus):defaultValue=1
_AtNtpPeerRowStatus_Type.__name__=_J
_AtNtpPeerRowStatus_Object=MibTableColumn
atNtpPeerRowStatus=_AtNtpPeerRowStatus_Object((1,3,6,1,4,1,207,8,4,4,4,502,7,1,7),_AtNtpPeerRowStatus_Type())
atNtpPeerRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:atNtpPeerRowStatus.setStatus(_A)
_AtNtpAssociationTable_Object=MibTable
atNtpAssociationTable=_AtNtpAssociationTable_Object((1,3,6,1,4,1,207,8,4,4,4,502,10))
if mibBuilder.loadTexts:atNtpAssociationTable.setStatus(_A)
_AtNtpAssociationEntry_Object=MibTableRow
atNtpAssociationEntry=_AtNtpAssociationEntry_Object((1,3,6,1,4,1,207,8,4,4,4,502,10,1))
atNtpAssociationEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:atNtpAssociationEntry.setStatus(_A)
_AtNtpAssociationIndex_Type=Integer32
_AtNtpAssociationIndex_Object=MibTableColumn
atNtpAssociationIndex=_AtNtpAssociationIndex_Object((1,3,6,1,4,1,207,8,4,4,4,502,10,1,1),_AtNtpAssociationIndex_Type())
atNtpAssociationIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:atNtpAssociationIndex.setStatus(_A)
_AtNtpAssociationPeerAddr_Type=DisplayString
_AtNtpAssociationPeerAddr_Object=MibTableColumn
atNtpAssociationPeerAddr=_AtNtpAssociationPeerAddr_Object((1,3,6,1,4,1,207,8,4,4,4,502,10,1,2),_AtNtpAssociationPeerAddr_Type())
atNtpAssociationPeerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpAssociationPeerAddr.setStatus(_A)
_AtNtpAssocaitionStatus_Type=DisplayString
_AtNtpAssocaitionStatus_Object=MibTableColumn
atNtpAssocaitionStatus=_AtNtpAssocaitionStatus_Object((1,3,6,1,4,1,207,8,4,4,4,502,10,1,3),_AtNtpAssocaitionStatus_Type())
atNtpAssocaitionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpAssocaitionStatus.setStatus(_A)
_AtNtpAssociationConfigured_Type=DisplayString
_AtNtpAssociationConfigured_Object=MibTableColumn
atNtpAssociationConfigured=_AtNtpAssociationConfigured_Object((1,3,6,1,4,1,207,8,4,4,4,502,10,1,4),_AtNtpAssociationConfigured_Type())
atNtpAssociationConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpAssociationConfigured.setStatus(_A)
_AtNtpAssociationRefClkAddr_Type=DisplayString
_AtNtpAssociationRefClkAddr_Object=MibTableColumn
atNtpAssociationRefClkAddr=_AtNtpAssociationRefClkAddr_Object((1,3,6,1,4,1,207,8,4,4,4,502,10,1,5),_AtNtpAssociationRefClkAddr_Type())
atNtpAssociationRefClkAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpAssociationRefClkAddr.setStatus(_A)
_AtNtpAssociationStratum_Type=Integer32
_AtNtpAssociationStratum_Object=MibTableColumn
atNtpAssociationStratum=_AtNtpAssociationStratum_Object((1,3,6,1,4,1,207,8,4,4,4,502,10,1,6),_AtNtpAssociationStratum_Type())
atNtpAssociationStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpAssociationStratum.setStatus(_A)
_AtNtpAssociationPoll_Type=Integer32
_AtNtpAssociationPoll_Object=MibTableColumn
atNtpAssociationPoll=_AtNtpAssociationPoll_Object((1,3,6,1,4,1,207,8,4,4,4,502,10,1,7),_AtNtpAssociationPoll_Type())
atNtpAssociationPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpAssociationPoll.setStatus(_A)
if mibBuilder.loadTexts:atNtpAssociationPoll.setUnits('seconds')
_AtNtpAssociationReach_Type=Integer32
_AtNtpAssociationReach_Object=MibTableColumn
atNtpAssociationReach=_AtNtpAssociationReach_Object((1,3,6,1,4,1,207,8,4,4,4,502,10,1,8),_AtNtpAssociationReach_Type())
atNtpAssociationReach.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpAssociationReach.setStatus(_A)
_AtNtpAssociationDelay_Type=DisplayString
_AtNtpAssociationDelay_Object=MibTableColumn
atNtpAssociationDelay=_AtNtpAssociationDelay_Object((1,3,6,1,4,1,207,8,4,4,4,502,10,1,9),_AtNtpAssociationDelay_Type())
atNtpAssociationDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpAssociationDelay.setStatus(_A)
_AtNtpAssociationOffset_Type=DisplayString
_AtNtpAssociationOffset_Object=MibTableColumn
atNtpAssociationOffset=_AtNtpAssociationOffset_Object((1,3,6,1,4,1,207,8,4,4,4,502,10,1,10),_AtNtpAssociationOffset_Type())
atNtpAssociationOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpAssociationOffset.setStatus(_A)
_AtNtpAssociationDisp_Type=DisplayString
_AtNtpAssociationDisp_Object=MibTableColumn
atNtpAssociationDisp=_AtNtpAssociationDisp_Object((1,3,6,1,4,1,207,8,4,4,4,502,10,1,11),_AtNtpAssociationDisp_Type())
atNtpAssociationDisp.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpAssociationDisp.setStatus(_A)
_AtNtpStatus_ObjectIdentity=ObjectIdentity
atNtpStatus=_AtNtpStatus_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,502,11))
_AtNtpSysClockSync_Type=TruthValue
_AtNtpSysClockSync_Object=MibScalar
atNtpSysClockSync=_AtNtpSysClockSync_Object((1,3,6,1,4,1,207,8,4,4,4,502,11,1),_AtNtpSysClockSync_Type())
atNtpSysClockSync.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpSysClockSync.setStatus(_A)
_AtNtpSysStratum_Type=Integer32
_AtNtpSysStratum_Object=MibScalar
atNtpSysStratum=_AtNtpSysStratum_Object((1,3,6,1,4,1,207,8,4,4,4,502,11,2),_AtNtpSysStratum_Type())
atNtpSysStratum.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpSysStratum.setStatus(_A)
_AtNtpSysReference_Type=DisplayString
_AtNtpSysReference_Object=MibScalar
atNtpSysReference=_AtNtpSysReference_Object((1,3,6,1,4,1,207,8,4,4,4,502,11,3),_AtNtpSysReference_Type())
atNtpSysReference.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpSysReference.setStatus(_A)
_AtNtpSysFrequency_Type=Integer32
_AtNtpSysFrequency_Object=MibScalar
atNtpSysFrequency=_AtNtpSysFrequency_Object((1,3,6,1,4,1,207,8,4,4,4,502,11,4),_AtNtpSysFrequency_Type())
atNtpSysFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpSysFrequency.setStatus(_A)
if mibBuilder.loadTexts:atNtpSysFrequency.setUnits('Hz')
_AtNtpSysPrecision_Type=Integer32
_AtNtpSysPrecision_Object=MibScalar
atNtpSysPrecision=_AtNtpSysPrecision_Object((1,3,6,1,4,1,207,8,4,4,4,502,11,5),_AtNtpSysPrecision_Type())
atNtpSysPrecision.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpSysPrecision.setStatus(_A)
class _AtNtpSysRefTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_AtNtpSysRefTime_Type.__name__=_G
_AtNtpSysRefTime_Object=MibScalar
atNtpSysRefTime=_AtNtpSysRefTime_Object((1,3,6,1,4,1,207,8,4,4,4,502,11,6),_AtNtpSysRefTime_Type())
atNtpSysRefTime.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpSysRefTime.setStatus(_A)
_AtNtpSysClkOffset_Type=Integer32
_AtNtpSysClkOffset_Object=MibScalar
atNtpSysClkOffset=_AtNtpSysClkOffset_Object((1,3,6,1,4,1,207,8,4,4,4,502,11,7),_AtNtpSysClkOffset_Type())
atNtpSysClkOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpSysClkOffset.setStatus(_A)
if mibBuilder.loadTexts:atNtpSysClkOffset.setUnits(_F)
_AtNtpSysRootDelay_Type=Integer32
_AtNtpSysRootDelay_Object=MibScalar
atNtpSysRootDelay=_AtNtpSysRootDelay_Object((1,3,6,1,4,1,207,8,4,4,4,502,11,8),_AtNtpSysRootDelay_Type())
atNtpSysRootDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpSysRootDelay.setStatus(_A)
if mibBuilder.loadTexts:atNtpSysRootDelay.setUnits(_F)
_AtNtpSysRootDisp_Type=Integer32
_AtNtpSysRootDisp_Object=MibScalar
atNtpSysRootDisp=_AtNtpSysRootDisp_Object((1,3,6,1,4,1,207,8,4,4,4,502,11,9),_AtNtpSysRootDisp_Type())
atNtpSysRootDisp.setMaxAccess(_B)
if mibBuilder.loadTexts:atNtpSysRootDisp.setStatus(_A)
if mibBuilder.loadTexts:atNtpSysRootDisp.setUnits(_F)
mibBuilder.exportSymbols(_E,**{'atNtp':atNtp,'atNtpPeerIndexNext':atNtpPeerIndexNext,'atNtpPeerTable':atNtpPeerTable,'atNtpPeerEntry':atNtpPeerEntry,_K:atNtpPeerIndex,'atNtpPeerNameAddr':atNtpPeerNameAddr,'atNtpPeerMode':atNtpPeerMode,'atNtpPeerPreference':atNtpPeerPreference,'atNtpPeerVersion':atNtpPeerVersion,'atNtpPeerKeyNumber':atNtpPeerKeyNumber,'atNtpPeerRowStatus':atNtpPeerRowStatus,'atNtpAssociationTable':atNtpAssociationTable,'atNtpAssociationEntry':atNtpAssociationEntry,_M:atNtpAssociationIndex,'atNtpAssociationPeerAddr':atNtpAssociationPeerAddr,'atNtpAssocaitionStatus':atNtpAssocaitionStatus,'atNtpAssociationConfigured':atNtpAssociationConfigured,'atNtpAssociationRefClkAddr':atNtpAssociationRefClkAddr,'atNtpAssociationStratum':atNtpAssociationStratum,'atNtpAssociationPoll':atNtpAssociationPoll,'atNtpAssociationReach':atNtpAssociationReach,'atNtpAssociationDelay':atNtpAssociationDelay,'atNtpAssociationOffset':atNtpAssociationOffset,'atNtpAssociationDisp':atNtpAssociationDisp,'atNtpStatus':atNtpStatus,'atNtpSysClockSync':atNtpSysClockSync,'atNtpSysStratum':atNtpSysStratum,'atNtpSysReference':atNtpSysReference,'atNtpSysFrequency':atNtpSysFrequency,'atNtpSysPrecision':atNtpSysPrecision,'atNtpSysRefTime':atNtpSysRefTime,'atNtpSysClkOffset':atNtpSysClkOffset,'atNtpSysRootDelay':atNtpSysRootDelay,'atNtpSysRootDisp':atNtpSysRootDisp})