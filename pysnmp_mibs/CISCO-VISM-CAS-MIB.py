_Y='ciscoVismCasXgcpVariantGroup'
_X='ciscoVismCasVariantGroup'
_W='vismCasCountryCode'
_V='vismCasTRinging'
_U='vismCasXgcpMaxRetries'
_T='vismCasXgcpInitialReXmitTime'
_S='vismCasXgcpMaxReXmitTime'
_R='vismCasXgcpFileName'
_Q='vismCasVariantSource'
_P='vismCasRowStatus'
_O='vismCasVariantState'
_N='vismCasInterdigitTMF'
_M='vismCasInterdigitTcrit'
_L='vismCasInterdigitTpart'
_K='vismCasDigitMethod'
_J='vismCasFileName'
_I='vismCasXgcpVariantName'
_H='deprecated'
_G='vismCasVariantName'
_F='DisplayString'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='CISCO-VISM-CAS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
voice,=mibBuilder.importSymbols('BASIS-MIB','voice')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
ciscoVismCasMIB=ModuleIdentity((1,3,6,1,4,1,351,150,88))
if mibBuilder.loadTexts:ciscoVismCasMIB.setRevisions(('2003-07-16 00:00',))
_VismCasGrp_ObjectIdentity=ObjectIdentity
vismCasGrp=_VismCasGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,8))
_VismCasVariantTable_Object=MibTable
vismCasVariantTable=_VismCasVariantTable_Object((1,3,6,1,4,1,351,110,5,5,8,1))
if mibBuilder.loadTexts:vismCasVariantTable.setStatus(_A)
_VismCasVariantEntry_Object=MibTableRow
vismCasVariantEntry=_VismCasVariantEntry_Object((1,3,6,1,4,1,351,110,5,5,8,1,1))
vismCasVariantEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:vismCasVariantEntry.setStatus(_A)
_VismCasVariantName_Type=DisplayString
_VismCasVariantName_Object=MibTableColumn
vismCasVariantName=_VismCasVariantName_Object((1,3,6,1,4,1,351,110,5,5,8,1,1,1),_VismCasVariantName_Type())
vismCasVariantName.setMaxAccess(_E)
if mibBuilder.loadTexts:vismCasVariantName.setStatus(_A)
class _VismCasFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,64))
_VismCasFileName_Type.__name__=_F
_VismCasFileName_Object=MibTableColumn
vismCasFileName=_VismCasFileName_Object((1,3,6,1,4,1,351,110,5,5,8,1,1,2),_VismCasFileName_Type())
vismCasFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCasFileName.setStatus(_A)
class _VismCasTRinging_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,600))
_VismCasTRinging_Type.__name__=_C
_VismCasTRinging_Object=MibTableColumn
vismCasTRinging=_VismCasTRinging_Object((1,3,6,1,4,1,351,110,5,5,8,1,1,3),_VismCasTRinging_Type())
vismCasTRinging.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCasTRinging.setStatus(_H)
class _VismCasDigitMethod_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mf',1),('dtmf',2)))
_VismCasDigitMethod_Type.__name__=_C
_VismCasDigitMethod_Object=MibTableColumn
vismCasDigitMethod=_VismCasDigitMethod_Object((1,3,6,1,4,1,351,110,5,5,8,1,1,4),_VismCasDigitMethod_Type())
vismCasDigitMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCasDigitMethod.setStatus(_A)
class _VismCasInterdigitTpart_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10000))
_VismCasInterdigitTpart_Type.__name__=_C
_VismCasInterdigitTpart_Object=MibTableColumn
vismCasInterdigitTpart=_VismCasInterdigitTpart_Object((1,3,6,1,4,1,351,110,5,5,8,1,1,5),_VismCasInterdigitTpart_Type())
vismCasInterdigitTpart.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCasInterdigitTpart.setStatus(_A)
class _VismCasInterdigitTcrit_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_VismCasInterdigitTcrit_Type.__name__=_C
_VismCasInterdigitTcrit_Object=MibTableColumn
vismCasInterdigitTcrit=_VismCasInterdigitTcrit_Object((1,3,6,1,4,1,351,110,5,5,8,1,1,6),_VismCasInterdigitTcrit_Type())
vismCasInterdigitTcrit.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCasInterdigitTcrit.setStatus(_A)
class _VismCasInterdigitTMF_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_VismCasInterdigitTMF_Type.__name__=_C
_VismCasInterdigitTMF_Object=MibTableColumn
vismCasInterdigitTMF=_VismCasInterdigitTMF_Object((1,3,6,1,4,1,351,110,5,5,8,1,1,7),_VismCasInterdigitTMF_Type())
vismCasInterdigitTMF.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCasInterdigitTMF.setStatus(_A)
class _VismCasVariantState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notConfigured',1),('configInProgress',2),('configured',3)))
_VismCasVariantState_Type.__name__=_C
_VismCasVariantState_Object=MibTableColumn
vismCasVariantState=_VismCasVariantState_Object((1,3,6,1,4,1,351,110,5,5,8,1,1,8),_VismCasVariantState_Type())
vismCasVariantState.setMaxAccess(_E)
if mibBuilder.loadTexts:vismCasVariantState.setStatus(_A)
class _VismCasRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*(('active',1),('createAndGo',4),('destroy',6)))
_VismCasRowStatus_Type.__name__=_C
_VismCasRowStatus_Object=MibTableColumn
vismCasRowStatus=_VismCasRowStatus_Object((1,3,6,1,4,1,351,110,5,5,8,1,1,9),_VismCasRowStatus_Type())
vismCasRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCasRowStatus.setStatus(_A)
class _VismCasCountryCode_Type(DisplayString):defaultValue=OctetString('US');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_VismCasCountryCode_Type.__name__=_F
_VismCasCountryCode_Object=MibTableColumn
vismCasCountryCode=_VismCasCountryCode_Object((1,3,6,1,4,1,351,110,5,5,8,1,1,10),_VismCasCountryCode_Type())
vismCasCountryCode.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCasCountryCode.setStatus(_H)
class _VismCasVariantSource_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unspecified',1),('internal',2),('external',3)))
_VismCasVariantSource_Type.__name__=_C
_VismCasVariantSource_Object=MibTableColumn
vismCasVariantSource=_VismCasVariantSource_Object((1,3,6,1,4,1,351,110,5,5,8,1,1,11),_VismCasVariantSource_Type())
vismCasVariantSource.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCasVariantSource.setStatus(_A)
_VismCasXgcpVariantTable_Object=MibTable
vismCasXgcpVariantTable=_VismCasXgcpVariantTable_Object((1,3,6,1,4,1,351,110,5,5,8,2))
if mibBuilder.loadTexts:vismCasXgcpVariantTable.setStatus(_A)
_VismCasXgcpVariantEntry_Object=MibTableRow
vismCasXgcpVariantEntry=_VismCasXgcpVariantEntry_Object((1,3,6,1,4,1,351,110,5,5,8,2,1))
vismCasXgcpVariantEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:vismCasXgcpVariantEntry.setStatus(_A)
_VismCasXgcpVariantName_Type=DisplayString
_VismCasXgcpVariantName_Object=MibTableColumn
vismCasXgcpVariantName=_VismCasXgcpVariantName_Object((1,3,6,1,4,1,351,110,5,5,8,2,1,1),_VismCasXgcpVariantName_Type())
vismCasXgcpVariantName.setMaxAccess(_E)
if mibBuilder.loadTexts:vismCasXgcpVariantName.setStatus(_A)
_VismCasXgcpFileName_Type=DisplayString
_VismCasXgcpFileName_Object=MibTableColumn
vismCasXgcpFileName=_VismCasXgcpFileName_Object((1,3,6,1,4,1,351,110,5,5,8,2,1,2),_VismCasXgcpFileName_Type())
vismCasXgcpFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:vismCasXgcpFileName.setStatus(_A)
class _VismCasXgcpMaxReXmitTime_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10000))
_VismCasXgcpMaxReXmitTime_Type.__name__=_C
_VismCasXgcpMaxReXmitTime_Object=MibTableColumn
vismCasXgcpMaxReXmitTime=_VismCasXgcpMaxReXmitTime_Object((1,3,6,1,4,1,351,110,5,5,8,2,1,3),_VismCasXgcpMaxReXmitTime_Type())
vismCasXgcpMaxReXmitTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCasXgcpMaxReXmitTime.setStatus(_A)
class _VismCasXgcpInitialReXmitTime_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10000))
_VismCasXgcpInitialReXmitTime_Type.__name__=_C
_VismCasXgcpInitialReXmitTime_Object=MibTableColumn
vismCasXgcpInitialReXmitTime=_VismCasXgcpInitialReXmitTime_Object((1,3,6,1,4,1,351,110,5,5,8,2,1,4),_VismCasXgcpInitialReXmitTime_Type())
vismCasXgcpInitialReXmitTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCasXgcpInitialReXmitTime.setStatus(_A)
class _VismCasXgcpMaxRetries_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_VismCasXgcpMaxRetries_Type.__name__=_C
_VismCasXgcpMaxRetries_Object=MibTableColumn
vismCasXgcpMaxRetries=_VismCasXgcpMaxRetries_Object((1,3,6,1,4,1,351,110,5,5,8,2,1,5),_VismCasXgcpMaxRetries_Type())
vismCasXgcpMaxRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:vismCasXgcpMaxRetries.setStatus(_A)
_CiscoVismCasMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVismCasMIBConformance=_CiscoVismCasMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,88,2))
_CiscoVismCasMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVismCasMIBGroups=_CiscoVismCasMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,88,2,1))
_CiscoVismCasMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVismCasMIBCompliances=_CiscoVismCasMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,88,2,2))
ciscoVismCasVariantGroup=ObjectGroup((1,3,6,1,4,1,351,150,88,2,1,1))
ciscoVismCasVariantGroup.setObjects(*((_B,_G),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciscoVismCasVariantGroup.setStatus(_A)
ciscoVismCasXgcpVariantGroup=ObjectGroup((1,3,6,1,4,1,351,150,88,2,1,2))
ciscoVismCasXgcpVariantGroup.setObjects(*((_B,_I),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoVismCasXgcpVariantGroup.setStatus(_A)
cvcVariantDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,351,150,88,2,1,3))
cvcVariantDeprecatedGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:cvcVariantDeprecatedGroup.setStatus(_H)
ciscoVismCasCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,88,2,2,1))
ciscoVismCasCompliance.setObjects(*((_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ciscoVismCasCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vismCasGrp':vismCasGrp,'vismCasVariantTable':vismCasVariantTable,'vismCasVariantEntry':vismCasVariantEntry,_G:vismCasVariantName,_J:vismCasFileName,_V:vismCasTRinging,_K:vismCasDigitMethod,_L:vismCasInterdigitTpart,_M:vismCasInterdigitTcrit,_N:vismCasInterdigitTMF,_O:vismCasVariantState,_P:vismCasRowStatus,_W:vismCasCountryCode,_Q:vismCasVariantSource,'vismCasXgcpVariantTable':vismCasXgcpVariantTable,'vismCasXgcpVariantEntry':vismCasXgcpVariantEntry,_I:vismCasXgcpVariantName,_R:vismCasXgcpFileName,_S:vismCasXgcpMaxReXmitTime,_T:vismCasXgcpInitialReXmitTime,_U:vismCasXgcpMaxRetries,'ciscoVismCasMIB':ciscoVismCasMIB,'ciscoVismCasMIBConformance':ciscoVismCasMIBConformance,'ciscoVismCasMIBGroups':ciscoVismCasMIBGroups,_X:ciscoVismCasVariantGroup,_Y:ciscoVismCasXgcpVariantGroup,'cvcVariantDeprecatedGroup':cvcVariantDeprecatedGroup,'ciscoVismCasMIBCompliances':ciscoVismCasMIBCompliances,'ciscoVismCasCompliance':ciscoVismCasCompliance})