_J='hpnsaEccMemErrIndex'
_I='hpnsaEccAgentIndex'
_H='NotificationType'
_G='OctetString'
_F='HPNSAECC-MIB'
_E='DisplayString'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_H,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_H,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaECC_ObjectIdentity=ObjectIdentity
hpnsaECC=_HpnsaECC_ObjectIdentity((1,3,6,1,4,1,11,2,23,6))
_HpnsaEccMibRev_ObjectIdentity=ObjectIdentity
hpnsaEccMibRev=_HpnsaEccMibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,6,1))
class _HpnsaEccMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaEccMibRevMajor_Type.__name__=_C
_HpnsaEccMibRevMajor_Object=MibScalar
hpnsaEccMibRevMajor=_HpnsaEccMibRevMajor_Object((1,3,6,1,4,1,11,2,23,6,1,1),_HpnsaEccMibRevMajor_Type())
hpnsaEccMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEccMibRevMajor.setStatus(_A)
class _HpnsaEccMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaEccMibRevMinor_Type.__name__=_C
_HpnsaEccMibRevMinor_Object=MibScalar
hpnsaEccMibRevMinor=_HpnsaEccMibRevMinor_Object((1,3,6,1,4,1,11,2,23,6,1,2),_HpnsaEccMibRevMinor_Type())
hpnsaEccMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEccMibRevMinor.setStatus(_A)
_HpnsaEccAgent_ObjectIdentity=ObjectIdentity
hpnsaEccAgent=_HpnsaEccAgent_ObjectIdentity((1,3,6,1,4,1,11,2,23,6,2))
_HpnsaEccAgentTable_Object=MibTable
hpnsaEccAgentTable=_HpnsaEccAgentTable_Object((1,3,6,1,4,1,11,2,23,6,2,1))
if mibBuilder.loadTexts:hpnsaEccAgentTable.setStatus(_A)
_HpnsaEccAgentEntry_Object=MibTableRow
hpnsaEccAgentEntry=_HpnsaEccAgentEntry_Object((1,3,6,1,4,1,11,2,23,6,2,1,1))
hpnsaEccAgentEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:hpnsaEccAgentEntry.setStatus(_A)
class _HpnsaEccAgentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaEccAgentIndex_Type.__name__=_C
_HpnsaEccAgentIndex_Object=MibTableColumn
hpnsaEccAgentIndex=_HpnsaEccAgentIndex_Object((1,3,6,1,4,1,11,2,23,6,2,1,1,1),_HpnsaEccAgentIndex_Type())
hpnsaEccAgentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEccAgentIndex.setStatus(_A)
class _HpnsaEccAgentName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaEccAgentName_Type.__name__=_E
_HpnsaEccAgentName_Object=MibTableColumn
hpnsaEccAgentName=_HpnsaEccAgentName_Object((1,3,6,1,4,1,11,2,23,6,2,1,1,2),_HpnsaEccAgentName_Type())
hpnsaEccAgentName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEccAgentName.setStatus(_A)
class _HpnsaEccAgentVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_HpnsaEccAgentVersion_Type.__name__=_E
_HpnsaEccAgentVersion_Object=MibTableColumn
hpnsaEccAgentVersion=_HpnsaEccAgentVersion_Object((1,3,6,1,4,1,11,2,23,6,2,1,1,3),_HpnsaEccAgentVersion_Type())
hpnsaEccAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEccAgentVersion.setStatus(_A)
class _HpnsaEccAgentDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HpnsaEccAgentDate_Type.__name__=_G
_HpnsaEccAgentDate_Object=MibTableColumn
hpnsaEccAgentDate=_HpnsaEccAgentDate_Object((1,3,6,1,4,1,11,2,23,6,2,1,1,4),_HpnsaEccAgentDate_Type())
hpnsaEccAgentDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEccAgentDate.setStatus(_A)
_HpnsaEccLog_ObjectIdentity=ObjectIdentity
hpnsaEccLog=_HpnsaEccLog_ObjectIdentity((1,3,6,1,4,1,11,2,23,6,3))
class _HpnsaEccStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notSupported',1),('disabled',2),('enabled',3)))
_HpnsaEccStatus_Type.__name__=_C
_HpnsaEccStatus_Object=MibScalar
hpnsaEccStatus=_HpnsaEccStatus_Object((1,3,6,1,4,1,11,2,23,6,3,1),_HpnsaEccStatus_Type())
hpnsaEccStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEccStatus.setStatus(_A)
_HpnsaEccEraseLog_Type=Integer32
_HpnsaEccEraseLog_Object=MibScalar
hpnsaEccEraseLog=_HpnsaEccEraseLog_Object((1,3,6,1,4,1,11,2,23,6,3,2),_HpnsaEccEraseLog_Type())
hpnsaEccEraseLog.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEccEraseLog.setStatus(_A)
_HpnsaEccTotalErrCorrected_Type=Integer32
_HpnsaEccTotalErrCorrected_Object=MibScalar
hpnsaEccTotalErrCorrected=_HpnsaEccTotalErrCorrected_Object((1,3,6,1,4,1,11,2,23,6,3,3),_HpnsaEccTotalErrCorrected_Type())
hpnsaEccTotalErrCorrected.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEccTotalErrCorrected.setStatus(_A)
class _HpnsaEccTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('trapOff',0),('trapOn',1)))
_HpnsaEccTrapEnable_Type.__name__=_C
_HpnsaEccTrapEnable_Object=MibScalar
hpnsaEccTrapEnable=_HpnsaEccTrapEnable_Object((1,3,6,1,4,1,11,2,23,6,3,4),_HpnsaEccTrapEnable_Type())
hpnsaEccTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEccTrapEnable.setStatus(_A)
class _HpnsaEccTrapDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_HpnsaEccTrapDelay_Type.__name__=_C
_HpnsaEccTrapDelay_Object=MibScalar
hpnsaEccTrapDelay=_HpnsaEccTrapDelay_Object((1,3,6,1,4,1,11,2,23,6,3,5),_HpnsaEccTrapDelay_Type())
hpnsaEccTrapDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEccTrapDelay.setStatus(_A)
class _HpnsaEccPollTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,2592000))
_HpnsaEccPollTime_Type.__name__=_C
_HpnsaEccPollTime_Object=MibScalar
hpnsaEccPollTime=_HpnsaEccPollTime_Object((1,3,6,1,4,1,11,2,23,6,3,6),_HpnsaEccPollTime_Type())
hpnsaEccPollTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnsaEccPollTime.setStatus(_A)
_HpnsaEccMemErrTable_Object=MibTable
hpnsaEccMemErrTable=_HpnsaEccMemErrTable_Object((1,3,6,1,4,1,11,2,23,6,3,7))
if mibBuilder.loadTexts:hpnsaEccMemErrTable.setStatus(_A)
_HpnsaEccMemErrEntry_Object=MibTableRow
hpnsaEccMemErrEntry=_HpnsaEccMemErrEntry_Object((1,3,6,1,4,1,11,2,23,6,3,7,1))
hpnsaEccMemErrEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:hpnsaEccMemErrEntry.setStatus(_A)
_HpnsaEccMemErrIndex_Type=Integer32
_HpnsaEccMemErrIndex_Object=MibTableColumn
hpnsaEccMemErrIndex=_HpnsaEccMemErrIndex_Object((1,3,6,1,4,1,11,2,23,6,3,7,1,1),_HpnsaEccMemErrIndex_Type())
hpnsaEccMemErrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEccMemErrIndex.setStatus(_A)
_HpnsaEccMemErrTime_Type=DisplayString
_HpnsaEccMemErrTime_Object=MibTableColumn
hpnsaEccMemErrTime=_HpnsaEccMemErrTime_Object((1,3,6,1,4,1,11,2,23,6,3,7,1,2),_HpnsaEccMemErrTime_Type())
hpnsaEccMemErrTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEccMemErrTime.setStatus(_A)
_HpnsaEccMemErrDesc_Type=DisplayString
_HpnsaEccMemErrDesc_Object=MibTableColumn
hpnsaEccMemErrDesc=_HpnsaEccMemErrDesc_Object((1,3,6,1,4,1,11,2,23,6,3,7,1,3),_HpnsaEccMemErrDesc_Type())
hpnsaEccMemErrDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaEccMemErrDesc.setStatus(_A)
hPECCMemory1=NotificationType((1,3,6,1,4,1,11,2,23,6,0,4353))
if mibBuilder.loadTexts:hPECCMemory1.setStatus('')
hPECCMemory4=NotificationType((1,3,6,1,4,1,11,2,23,6,0,4354))
if mibBuilder.loadTexts:hPECCMemory4.setStatus('')
hPECCMemory5=NotificationType((1,3,6,1,4,1,11,2,23,6,0,4355))
if mibBuilder.loadTexts:hPECCMemory5.setStatus('')
hPECCMemory6=NotificationType((1,3,6,1,4,1,11,2,23,6,0,4357))
if mibBuilder.loadTexts:hPECCMemory6.setStatus('')
hPECCMemory8=NotificationType((1,3,6,1,4,1,11,2,23,6,0,4358))
if mibBuilder.loadTexts:hPECCMemory8.setStatus('')
mibBuilder.exportSymbols(_F,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaECC':hpnsaECC,'hPECCMemory1':hPECCMemory1,'hPECCMemory4':hPECCMemory4,'hPECCMemory5':hPECCMemory5,'hPECCMemory6':hPECCMemory6,'hPECCMemory8':hPECCMemory8,'hpnsaEccMibRev':hpnsaEccMibRev,'hpnsaEccMibRevMajor':hpnsaEccMibRevMajor,'hpnsaEccMibRevMinor':hpnsaEccMibRevMinor,'hpnsaEccAgent':hpnsaEccAgent,'hpnsaEccAgentTable':hpnsaEccAgentTable,'hpnsaEccAgentEntry':hpnsaEccAgentEntry,_I:hpnsaEccAgentIndex,'hpnsaEccAgentName':hpnsaEccAgentName,'hpnsaEccAgentVersion':hpnsaEccAgentVersion,'hpnsaEccAgentDate':hpnsaEccAgentDate,'hpnsaEccLog':hpnsaEccLog,'hpnsaEccStatus':hpnsaEccStatus,'hpnsaEccEraseLog':hpnsaEccEraseLog,'hpnsaEccTotalErrCorrected':hpnsaEccTotalErrCorrected,'hpnsaEccTrapEnable':hpnsaEccTrapEnable,'hpnsaEccTrapDelay':hpnsaEccTrapDelay,'hpnsaEccPollTime':hpnsaEccPollTime,'hpnsaEccMemErrTable':hpnsaEccMemErrTable,'hpnsaEccMemErrEntry':hpnsaEccMemErrEntry,_J:hpnsaEccMemErrIndex,'hpnsaEccMemErrTime':hpnsaEccMemErrTime,'hpnsaEccMemErrDesc':hpnsaEccMemErrDesc})