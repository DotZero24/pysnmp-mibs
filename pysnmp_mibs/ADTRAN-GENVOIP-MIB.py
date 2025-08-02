_A0='adGenVoipUserHotlineStatusEntryIndex'
_z='adGenVoipUserReverseLookupTableEntryIndex'
_y='adGenVoipCallFeatureProfileEntryIndex'
_x='adGenVoipMediaProfileProvEntryIndex'
_w='AdGenVoipCodecProfileType'
_v='adGenVoipCodecProfileProvIndex'
_u='adGenVoipDialingProfileCommonProvEntryIndex'
_t='remove'
_s='adGenVoipDialingProfileProvExtEntryIndex'
_r='adGenVoipDialingProfileExternalLineCodeEntryIndex'
_q='adGenVoipDialingProfileSPREPatternEntryIndex'
_p='adGenVoipDialingProfileDialPlanPatternEntryIndex'
_o='ignore'
_n='adGenVoipUserEntryIndex'
_m='adGenVoipCallServiceClassEntryIndex'
_l='adGenVoipSPREPatternEntryIndex'
_k='required'
_j='prohibited'
_i='optional'
_h='notEmergencyNumber'
_g='isEmergencyNumber'
_f='specifyCarrier'
_e='operatorAssisted'
_d='international'
_c='a900Number'
_b='tollFree'
_a='national'
_Z='extensions'
_Y='alwaysPermitted'
_X='adGenVoipDialPlanPatternEntryIndex'
_W='adGenVoipTrunkEntryIndex'
_V='ifIndex'
_U='IF-MIB'
_T='adGenVoipCodecProfileNameProvIndex'
_S='network'
_R='stutterDial'
_Q='dial'
_P='none'
_O='milliseconds'
_N='deprecated'
_M='local'
_L='enabled'
_K='TruthValue'
_J='disabled'
_I='Unsigned32'
_H='not-accessible'
_G='DisplayString'
_F='ADTRAN-GENVOIP-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenVoip,adGenVoipID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenVoip','adGenVoipID')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_U,'InterfaceIndexOrZero',_V)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention',_K)
adGenVoipIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,20,1))
if mibBuilder.loadTexts:adGenVoipIdentity.setRevisions(('2021-11-02 00:00','2019-10-08 00:00','2019-07-31 00:00','2019-04-24 00:00','2019-04-04 00:00','2018-04-11 00:00','2018-01-08 00:00','2017-09-08 00:00','2014-10-31 00:00','2014-09-30 00:00','2014-02-26 00:00','2013-08-28 00:00','2013-05-13 00:00','2012-11-19 00:00','2012-11-08 00:00','2012-10-31 00:00','2012-07-23 00:00','2012-07-10 00:00','2011-06-13 00:00','2011-03-03 00:00','2009-10-06 00:00'))
class AdGenVoipTrunkName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
class AdGenVoipCallServiceClassName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
class AdGenVoipUserNumber(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
class AdGenVoipDialingProfileName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
class AdGenVoipCodecProfileName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
class AdGenVoipMediaProfileName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
class AdGenVoipCodecProfileType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_P,0),('g711ulaw',1),('g711alaw',2),('g729',3)))
class AdGenVoipCallFeatureProfileName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
class AdGenVoipCallReverseLookupIfIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_AdGenVoipProvisioning_ObjectIdentity=ObjectIdentity
adGenVoipProvisioning=_AdGenVoipProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1))
_AdGenVoipTrunkProv_ObjectIdentity=ObjectIdentity
adGenVoipTrunkProv=_AdGenVoipTrunkProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,1))
_AdGenVoipTrunkProvTable_Object=MibTable
adGenVoipTrunkProvTable=_AdGenVoipTrunkProvTable_Object((1,3,6,1,4,1,664,5,70,20,1,1,1))
if mibBuilder.loadTexts:adGenVoipTrunkProvTable.setStatus(_A)
_AdGenVoipTrunkProvEntry_Object=MibTableRow
adGenVoipTrunkProvEntry=_AdGenVoipTrunkProvEntry_Object((1,3,6,1,4,1,664,5,70,20,1,1,1,1))
adGenVoipTrunkProvEntry.setIndexNames((0,_F,_W))
if mibBuilder.loadTexts:adGenVoipTrunkProvEntry.setStatus(_A)
_AdGenVoipTrunkEntryIndex_Type=AdGenVoipTrunkName
_AdGenVoipTrunkEntryIndex_Object=MibTableColumn
adGenVoipTrunkEntryIndex=_AdGenVoipTrunkEntryIndex_Object((1,3,6,1,4,1,664,5,70,20,1,1,1,1,1),_AdGenVoipTrunkEntryIndex_Type())
adGenVoipTrunkEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVoipTrunkEntryIndex.setStatus(_A)
class _AdGenVoipTrunkTransfer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('blind',1),('unattended',2)))
_AdGenVoipTrunkTransfer_Type.__name__=_D
_AdGenVoipTrunkTransfer_Object=MibTableColumn
adGenVoipTrunkTransfer=_AdGenVoipTrunkTransfer_Object((1,3,6,1,4,1,664,5,70,20,1,1,1,1,2),_AdGenVoipTrunkTransfer_Type())
adGenVoipTrunkTransfer.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipTrunkTransfer.setStatus(_A)
_AdGenVoipDialPlanProv_ObjectIdentity=ObjectIdentity
adGenVoipDialPlanProv=_AdGenVoipDialPlanProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,2))
_AdGenVoipDialPlanProvCurrentNumber_Type=Integer32
_AdGenVoipDialPlanProvCurrentNumber_Object=MibScalar
adGenVoipDialPlanProvCurrentNumber=_AdGenVoipDialPlanProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,20,1,2,1),_AdGenVoipDialPlanProvCurrentNumber_Type())
adGenVoipDialPlanProvCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialPlanProvCurrentNumber.setStatus(_A)
_AdGenVoipDialPlanProvLastCreateError_Type=DisplayString
_AdGenVoipDialPlanProvLastCreateError_Object=MibScalar
adGenVoipDialPlanProvLastCreateError=_AdGenVoipDialPlanProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,20,1,2,2),_AdGenVoipDialPlanProvLastCreateError_Type())
adGenVoipDialPlanProvLastCreateError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialPlanProvLastCreateError.setStatus(_A)
_AdGenVoipDialPlanProvTable_Object=MibTable
adGenVoipDialPlanProvTable=_AdGenVoipDialPlanProvTable_Object((1,3,6,1,4,1,664,5,70,20,1,2,3))
if mibBuilder.loadTexts:adGenVoipDialPlanProvTable.setStatus(_A)
_AdGenVoipDialPlanProvEntry_Object=MibTableRow
adGenVoipDialPlanProvEntry=_AdGenVoipDialPlanProvEntry_Object((1,3,6,1,4,1,664,5,70,20,1,2,3,1))
adGenVoipDialPlanProvEntry.setIndexNames((1,_F,_X))
if mibBuilder.loadTexts:adGenVoipDialPlanProvEntry.setStatus(_A)
class _AdGenVoipDialPlanPatternEntryIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_AdGenVoipDialPlanPatternEntryIndex_Type.__name__=_G
_AdGenVoipDialPlanPatternEntryIndex_Object=MibTableColumn
adGenVoipDialPlanPatternEntryIndex=_AdGenVoipDialPlanPatternEntryIndex_Object((1,3,6,1,4,1,664,5,70,20,1,2,3,1,1),_AdGenVoipDialPlanPatternEntryIndex_Type())
adGenVoipDialPlanPatternEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVoipDialPlanPatternEntryIndex.setStatus(_A)
_AdGenVoipDialPlanRowStatus_Type=RowStatus
_AdGenVoipDialPlanRowStatus_Object=MibTableColumn
adGenVoipDialPlanRowStatus=_AdGenVoipDialPlanRowStatus_Object((1,3,6,1,4,1,664,5,70,20,1,2,3,1,2),_AdGenVoipDialPlanRowStatus_Type())
adGenVoipDialPlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialPlanRowStatus.setStatus(_A)
_AdGenVoipDialPlanLastErrorString_Type=DisplayString
_AdGenVoipDialPlanLastErrorString_Object=MibTableColumn
adGenVoipDialPlanLastErrorString=_AdGenVoipDialPlanLastErrorString_Object((1,3,6,1,4,1,664,5,70,20,1,2,3,1,3),_AdGenVoipDialPlanLastErrorString_Type())
adGenVoipDialPlanLastErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialPlanLastErrorString.setStatus(_A)
class _AdGenVoipDialPlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_M,3),(_a,4),(_b,5),(_c,6),(_d,7),(_e,8),(_f,9),('user1',10),('user2',11),('user3',12)))
_AdGenVoipDialPlanType_Type.__name__=_D
_AdGenVoipDialPlanType_Object=MibTableColumn
adGenVoipDialPlanType=_AdGenVoipDialPlanType_Object((1,3,6,1,4,1,664,5,70,20,1,2,3,1,4),_AdGenVoipDialPlanType_Type())
adGenVoipDialPlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialPlanType.setStatus(_A)
class _AdGenVoipDialPlanEmergencyNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_AdGenVoipDialPlanEmergencyNumber_Type.__name__=_D
_AdGenVoipDialPlanEmergencyNumber_Object=MibTableColumn
adGenVoipDialPlanEmergencyNumber=_AdGenVoipDialPlanEmergencyNumber_Object((1,3,6,1,4,1,664,5,70,20,1,2,3,1,5),_AdGenVoipDialPlanEmergencyNumber_Type())
adGenVoipDialPlanEmergencyNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialPlanEmergencyNumber.setStatus(_A)
class _AdGenVoipDialPlanExternalLineCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3)))
_AdGenVoipDialPlanExternalLineCode_Type.__name__=_D
_AdGenVoipDialPlanExternalLineCode_Object=MibTableColumn
adGenVoipDialPlanExternalLineCode=_AdGenVoipDialPlanExternalLineCode_Object((1,3,6,1,4,1,664,5,70,20,1,2,3,1,6),_AdGenVoipDialPlanExternalLineCode_Type())
adGenVoipDialPlanExternalLineCode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialPlanExternalLineCode.setStatus(_A)
_AdGenVoipSPREPatternProv_ObjectIdentity=ObjectIdentity
adGenVoipSPREPatternProv=_AdGenVoipSPREPatternProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,3))
_AdGenVoipSPREPatternProvCurrentNumber_Type=Integer32
_AdGenVoipSPREPatternProvCurrentNumber_Object=MibScalar
adGenVoipSPREPatternProvCurrentNumber=_AdGenVoipSPREPatternProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,20,1,3,1),_AdGenVoipSPREPatternProvCurrentNumber_Type())
adGenVoipSPREPatternProvCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipSPREPatternProvCurrentNumber.setStatus(_A)
_AdGenVoipSPREPatternProvLastCreateError_Type=DisplayString
_AdGenVoipSPREPatternProvLastCreateError_Object=MibScalar
adGenVoipSPREPatternProvLastCreateError=_AdGenVoipSPREPatternProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,20,1,3,2),_AdGenVoipSPREPatternProvLastCreateError_Type())
adGenVoipSPREPatternProvLastCreateError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipSPREPatternProvLastCreateError.setStatus(_A)
_AdGenVoipSPREPatternProvTable_Object=MibTable
adGenVoipSPREPatternProvTable=_AdGenVoipSPREPatternProvTable_Object((1,3,6,1,4,1,664,5,70,20,1,3,3))
if mibBuilder.loadTexts:adGenVoipSPREPatternProvTable.setStatus(_A)
_AdGenVoipSPREPatternProvEntry_Object=MibTableRow
adGenVoipSPREPatternProvEntry=_AdGenVoipSPREPatternProvEntry_Object((1,3,6,1,4,1,664,5,70,20,1,3,3,1))
adGenVoipSPREPatternProvEntry.setIndexNames((1,_F,_l))
if mibBuilder.loadTexts:adGenVoipSPREPatternProvEntry.setStatus(_A)
class _AdGenVoipSPREPatternEntryIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,44))
_AdGenVoipSPREPatternEntryIndex_Type.__name__=_G
_AdGenVoipSPREPatternEntryIndex_Object=MibTableColumn
adGenVoipSPREPatternEntryIndex=_AdGenVoipSPREPatternEntryIndex_Object((1,3,6,1,4,1,664,5,70,20,1,3,3,1,1),_AdGenVoipSPREPatternEntryIndex_Type())
adGenVoipSPREPatternEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVoipSPREPatternEntryIndex.setStatus(_A)
_AdGenVoipSPREPatternRowStatus_Type=RowStatus
_AdGenVoipSPREPatternRowStatus_Object=MibTableColumn
adGenVoipSPREPatternRowStatus=_AdGenVoipSPREPatternRowStatus_Object((1,3,6,1,4,1,664,5,70,20,1,3,3,1,2),_AdGenVoipSPREPatternRowStatus_Type())
adGenVoipSPREPatternRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipSPREPatternRowStatus.setStatus(_A)
_AdGenVoipSPREPatternLastErrorString_Type=DisplayString
_AdGenVoipSPREPatternLastErrorString_Object=MibTableColumn
adGenVoipSPREPatternLastErrorString=_AdGenVoipSPREPatternLastErrorString_Object((1,3,6,1,4,1,664,5,70,20,1,3,3,1,3),_AdGenVoipSPREPatternLastErrorString_Type())
adGenVoipSPREPatternLastErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipSPREPatternLastErrorString.setStatus(_A)
class _AdGenVoipSPREPatternTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3)))
_AdGenVoipSPREPatternTone_Type.__name__=_D
_AdGenVoipSPREPatternTone_Object=MibTableColumn
adGenVoipSPREPatternTone=_AdGenVoipSPREPatternTone_Object((1,3,6,1,4,1,664,5,70,20,1,3,3,1,4),_AdGenVoipSPREPatternTone_Type())
adGenVoipSPREPatternTone.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipSPREPatternTone.setStatus(_A)
_AdGenVoipCallServiceClassProv_ObjectIdentity=ObjectIdentity
adGenVoipCallServiceClassProv=_AdGenVoipCallServiceClassProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,4))
_AdGenVoipCallServiceClassProvCurrentNumber_Type=Integer32
_AdGenVoipCallServiceClassProvCurrentNumber_Object=MibScalar
adGenVoipCallServiceClassProvCurrentNumber=_AdGenVoipCallServiceClassProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,20,1,4,1),_AdGenVoipCallServiceClassProvCurrentNumber_Type())
adGenVoipCallServiceClassProvCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipCallServiceClassProvCurrentNumber.setStatus(_A)
_AdGenVoipCallServiceClassProvLastCreateError_Type=DisplayString
_AdGenVoipCallServiceClassProvLastCreateError_Object=MibScalar
adGenVoipCallServiceClassProvLastCreateError=_AdGenVoipCallServiceClassProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,20,1,4,2),_AdGenVoipCallServiceClassProvLastCreateError_Type())
adGenVoipCallServiceClassProvLastCreateError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipCallServiceClassProvLastCreateError.setStatus(_A)
_AdGenVoipCallServiceClassProvTable_Object=MibTable
adGenVoipCallServiceClassProvTable=_AdGenVoipCallServiceClassProvTable_Object((1,3,6,1,4,1,664,5,70,20,1,4,3))
if mibBuilder.loadTexts:adGenVoipCallServiceClassProvTable.setStatus(_A)
_AdGenVoipCallServiceClassProvEntry_Object=MibTableRow
adGenVoipCallServiceClassProvEntry=_AdGenVoipCallServiceClassProvEntry_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1))
adGenVoipCallServiceClassProvEntry.setIndexNames((1,_F,_m))
if mibBuilder.loadTexts:adGenVoipCallServiceClassProvEntry.setStatus(_A)
_AdGenVoipCallServiceClassEntryIndex_Type=AdGenVoipCallServiceClassName
_AdGenVoipCallServiceClassEntryIndex_Object=MibTableColumn
adGenVoipCallServiceClassEntryIndex=_AdGenVoipCallServiceClassEntryIndex_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,1),_AdGenVoipCallServiceClassEntryIndex_Type())
adGenVoipCallServiceClassEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVoipCallServiceClassEntryIndex.setStatus(_A)
_AdGenVoipCallServiceClassRowStatus_Type=RowStatus
_AdGenVoipCallServiceClassRowStatus_Object=MibTableColumn
adGenVoipCallServiceClassRowStatus=_AdGenVoipCallServiceClassRowStatus_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,2),_AdGenVoipCallServiceClassRowStatus_Type())
adGenVoipCallServiceClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceClassRowStatus.setStatus(_A)
_AdGenVoipCallServiceClassLastErrorString_Type=DisplayString
_AdGenVoipCallServiceClassLastErrorString_Object=MibTableColumn
adGenVoipCallServiceClassLastErrorString=_AdGenVoipCallServiceClassLastErrorString_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,3),_AdGenVoipCallServiceClassLastErrorString_Type())
adGenVoipCallServiceClassLastErrorString.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceClassLastErrorString.setStatus(_A)
_AdGenVoipCallServiceClass900Number_Type=TruthValue
_AdGenVoipCallServiceClass900Number_Object=MibTableColumn
adGenVoipCallServiceClass900Number=_AdGenVoipCallServiceClass900Number_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,4),_AdGenVoipCallServiceClass900Number_Type())
adGenVoipCallServiceClass900Number.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceClass900Number.setStatus(_A)
_AdGenVoipCallServiceClassExtensions_Type=TruthValue
_AdGenVoipCallServiceClassExtensions_Object=MibTableColumn
adGenVoipCallServiceClassExtensions=_AdGenVoipCallServiceClassExtensions_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,5),_AdGenVoipCallServiceClassExtensions_Type())
adGenVoipCallServiceClassExtensions.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceClassExtensions.setStatus(_A)
_AdGenVoipCallServiceClassInternational_Type=TruthValue
_AdGenVoipCallServiceClassInternational_Object=MibTableColumn
adGenVoipCallServiceClassInternational=_AdGenVoipCallServiceClassInternational_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,6),_AdGenVoipCallServiceClassInternational_Type())
adGenVoipCallServiceClassInternational.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceClassInternational.setStatus(_A)
_AdGenVoipCallServiceClassLocal_Type=TruthValue
_AdGenVoipCallServiceClassLocal_Object=MibTableColumn
adGenVoipCallServiceClassLocal=_AdGenVoipCallServiceClassLocal_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,7),_AdGenVoipCallServiceClassLocal_Type())
adGenVoipCallServiceClassLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceClassLocal.setStatus(_A)
_AdGenVoipCallServiceClassNational_Type=TruthValue
_AdGenVoipCallServiceClassNational_Object=MibTableColumn
adGenVoipCallServiceClassNational=_AdGenVoipCallServiceClassNational_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,8),_AdGenVoipCallServiceClassNational_Type())
adGenVoipCallServiceClassNational.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceClassNational.setStatus(_A)
_AdGenVoipCallServiceClassOperatorAssisted_Type=TruthValue
_AdGenVoipCallServiceClassOperatorAssisted_Object=MibTableColumn
adGenVoipCallServiceClassOperatorAssisted=_AdGenVoipCallServiceClassOperatorAssisted_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,9),_AdGenVoipCallServiceClassOperatorAssisted_Type())
adGenVoipCallServiceClassOperatorAssisted.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceClassOperatorAssisted.setStatus(_A)
_AdGenVoipCallServiceClassSpecifyCarrier_Type=TruthValue
_AdGenVoipCallServiceClassSpecifyCarrier_Object=MibTableColumn
adGenVoipCallServiceClassSpecifyCarrier=_AdGenVoipCallServiceClassSpecifyCarrier_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,10),_AdGenVoipCallServiceClassSpecifyCarrier_Type())
adGenVoipCallServiceClassSpecifyCarrier.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceClassSpecifyCarrier.setStatus(_A)
_AdGenVoipCallServiceClassTollFree_Type=TruthValue
_AdGenVoipCallServiceClassTollFree_Object=MibTableColumn
adGenVoipCallServiceClassTollFree=_AdGenVoipCallServiceClassTollFree_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,11),_AdGenVoipCallServiceClassTollFree_Type())
adGenVoipCallServiceClassTollFree.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceClassTollFree.setStatus(_A)
_AdGenVoipCallServiceClassUser1_Type=TruthValue
_AdGenVoipCallServiceClassUser1_Object=MibTableColumn
adGenVoipCallServiceClassUser1=_AdGenVoipCallServiceClassUser1_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,12),_AdGenVoipCallServiceClassUser1_Type())
adGenVoipCallServiceClassUser1.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceClassUser1.setStatus(_A)
_AdGenVoipCallServiceClassUser2_Type=TruthValue
_AdGenVoipCallServiceClassUser2_Object=MibTableColumn
adGenVoipCallServiceClassUser2=_AdGenVoipCallServiceClassUser2_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,13),_AdGenVoipCallServiceClassUser2_Type())
adGenVoipCallServiceClassUser2.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceClassUser2.setStatus(_A)
_AdGenVoipCallServiceClassUser3_Type=TruthValue
_AdGenVoipCallServiceClassUser3_Object=MibTableColumn
adGenVoipCallServiceClassUser3=_AdGenVoipCallServiceClassUser3_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,14),_AdGenVoipCallServiceClassUser3_Type())
adGenVoipCallServiceClassUser3.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceClassUser3.setStatus(_A)
_AdGenVoipCallServiceConference_Type=TruthValue
_AdGenVoipCallServiceConference_Object=MibTableColumn
adGenVoipCallServiceConference=_AdGenVoipCallServiceConference_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,15),_AdGenVoipCallServiceConference_Type())
adGenVoipCallServiceConference.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceConference.setStatus(_A)
_AdGenVoipCallServiceDisableCallWaiting_Type=TruthValue
_AdGenVoipCallServiceDisableCallWaiting_Object=MibTableColumn
adGenVoipCallServiceDisableCallWaiting=_AdGenVoipCallServiceDisableCallWaiting_Object((1,3,6,1,4,1,664,5,70,20,1,4,3,1,16),_AdGenVoipCallServiceDisableCallWaiting_Type())
adGenVoipCallServiceDisableCallWaiting.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallServiceDisableCallWaiting.setStatus(_A)
_AdGenVoipUserProv_ObjectIdentity=ObjectIdentity
adGenVoipUserProv=_AdGenVoipUserProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,5))
_AdGenVoipUserProvCurrentNumber_Type=Integer32
_AdGenVoipUserProvCurrentNumber_Object=MibScalar
adGenVoipUserProvCurrentNumber=_AdGenVoipUserProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,20,1,5,1),_AdGenVoipUserProvCurrentNumber_Type())
adGenVoipUserProvCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipUserProvCurrentNumber.setStatus(_A)
_AdGenVoipUserProvLastCreateError_Type=DisplayString
_AdGenVoipUserProvLastCreateError_Object=MibScalar
adGenVoipUserProvLastCreateError=_AdGenVoipUserProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,20,1,5,2),_AdGenVoipUserProvLastCreateError_Type())
adGenVoipUserProvLastCreateError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipUserProvLastCreateError.setStatus(_A)
_AdGenVoipUserProvTable_Object=MibTable
adGenVoipUserProvTable=_AdGenVoipUserProvTable_Object((1,3,6,1,4,1,664,5,70,20,1,5,3))
if mibBuilder.loadTexts:adGenVoipUserProvTable.setStatus(_A)
_AdGenVoipUserProvEntry_Object=MibTableRow
adGenVoipUserProvEntry=_AdGenVoipUserProvEntry_Object((1,3,6,1,4,1,664,5,70,20,1,5,3,1))
adGenVoipUserProvEntry.setIndexNames((0,_F,_n))
if mibBuilder.loadTexts:adGenVoipUserProvEntry.setStatus(_A)
_AdGenVoipUserEntryIndex_Type=AdGenVoipUserNumber
_AdGenVoipUserEntryIndex_Object=MibTableColumn
adGenVoipUserEntryIndex=_AdGenVoipUserEntryIndex_Object((1,3,6,1,4,1,664,5,70,20,1,5,3,1,1),_AdGenVoipUserEntryIndex_Type())
adGenVoipUserEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVoipUserEntryIndex.setStatus(_A)
_AdGenVoipUserRowStatus_Type=RowStatus
_AdGenVoipUserRowStatus_Object=MibTableColumn
adGenVoipUserRowStatus=_AdGenVoipUserRowStatus_Object((1,3,6,1,4,1,664,5,70,20,1,5,3,1,2),_AdGenVoipUserRowStatus_Type())
adGenVoipUserRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipUserRowStatus.setStatus(_A)
_AdGenVoipUserLastErrorString_Type=DisplayString
_AdGenVoipUserLastErrorString_Object=MibTableColumn
adGenVoipUserLastErrorString=_AdGenVoipUserLastErrorString_Object((1,3,6,1,4,1,664,5,70,20,1,5,3,1,3),_AdGenVoipUserLastErrorString_Type())
adGenVoipUserLastErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipUserLastErrorString.setStatus(_A)
_AdGenVoipUserFxsPort_Type=InterfaceIndexOrZero
_AdGenVoipUserFxsPort_Object=MibTableColumn
adGenVoipUserFxsPort=_AdGenVoipUserFxsPort_Object((1,3,6,1,4,1,664,5,70,20,1,5,3,1,4),_AdGenVoipUserFxsPort_Type())
adGenVoipUserFxsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipUserFxsPort.setStatus(_A)
_AdGenVoipUserCallClass_Type=AdGenVoipCallServiceClassName
_AdGenVoipUserCallClass_Object=MibTableColumn
adGenVoipUserCallClass=_AdGenVoipUserCallClass_Object((1,3,6,1,4,1,664,5,70,20,1,5,3,1,5),_AdGenVoipUserCallClass_Type())
adGenVoipUserCallClass.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipUserCallClass.setStatus(_A)
_AdGenVoipUserCallWaiting_Type=TruthValue
_AdGenVoipUserCallWaiting_Object=MibTableColumn
adGenVoipUserCallWaiting=_AdGenVoipUserCallWaiting_Object((1,3,6,1,4,1,664,5,70,20,1,5,3,1,6),_AdGenVoipUserCallWaiting_Type())
adGenVoipUserCallWaiting.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipUserCallWaiting.setStatus(_A)
_AdGenVoipUserDialingProfile_Type=AdGenVoipDialingProfileName
_AdGenVoipUserDialingProfile_Object=MibTableColumn
adGenVoipUserDialingProfile=_AdGenVoipUserDialingProfile_Object((1,3,6,1,4,1,664,5,70,20,1,5,3,1,7),_AdGenVoipUserDialingProfile_Type())
adGenVoipUserDialingProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipUserDialingProfile.setStatus(_A)
class _AdGenVoipUserHotlineEnabled_Type(TruthValue):defaultValue=2
_AdGenVoipUserHotlineEnabled_Type.__name__=_K
_AdGenVoipUserHotlineEnabled_Object=MibTableColumn
adGenVoipUserHotlineEnabled=_AdGenVoipUserHotlineEnabled_Object((1,3,6,1,4,1,664,5,70,20,1,5,3,1,8),_AdGenVoipUserHotlineEnabled_Type())
adGenVoipUserHotlineEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipUserHotlineEnabled.setStatus(_A)
class _AdGenVoipUserHotlineNumber_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AdGenVoipUserHotlineNumber_Type.__name__=_G
_AdGenVoipUserHotlineNumber_Object=MibTableColumn
adGenVoipUserHotlineNumber=_AdGenVoipUserHotlineNumber_Object((1,3,6,1,4,1,664,5,70,20,1,5,3,1,9),_AdGenVoipUserHotlineNumber_Type())
adGenVoipUserHotlineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipUserHotlineNumber.setStatus(_A)
class _AdGenVoipUserSipTrunkManualSelect_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_AdGenVoipUserSipTrunkManualSelect_Type.__name__=_G
_AdGenVoipUserSipTrunkManualSelect_Object=MibTableColumn
adGenVoipUserSipTrunkManualSelect=_AdGenVoipUserSipTrunkManualSelect_Object((1,3,6,1,4,1,664,5,70,20,1,5,3,1,10),_AdGenVoipUserSipTrunkManualSelect_Type())
adGenVoipUserSipTrunkManualSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipUserSipTrunkManualSelect.setStatus(_A)
class _AdGenVoipUserWarmlineEnabled_Type(TruthValue):defaultValue=2
_AdGenVoipUserWarmlineEnabled_Type.__name__=_K
_AdGenVoipUserWarmlineEnabled_Object=MibTableColumn
adGenVoipUserWarmlineEnabled=_AdGenVoipUserWarmlineEnabled_Object((1,3,6,1,4,1,664,5,70,20,1,5,3,1,11),_AdGenVoipUserWarmlineEnabled_Type())
adGenVoipUserWarmlineEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipUserWarmlineEnabled.setStatus(_A)
class _AdGenVoipUserWarmlineNumber_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AdGenVoipUserWarmlineNumber_Type.__name__=_G
_AdGenVoipUserWarmlineNumber_Object=MibTableColumn
adGenVoipUserWarmlineNumber=_AdGenVoipUserWarmlineNumber_Object((1,3,6,1,4,1,664,5,70,20,1,5,3,1,12),_AdGenVoipUserWarmlineNumber_Type())
adGenVoipUserWarmlineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipUserWarmlineNumber.setStatus(_A)
class _AdGenVoipUserWarmlineDelay_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_AdGenVoipUserWarmlineDelay_Type.__name__=_D
_AdGenVoipUserWarmlineDelay_Object=MibTableColumn
adGenVoipUserWarmlineDelay=_AdGenVoipUserWarmlineDelay_Object((1,3,6,1,4,1,664,5,70,20,1,5,3,1,13),_AdGenVoipUserWarmlineDelay_Type())
adGenVoipUserWarmlineDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipUserWarmlineDelay.setStatus(_A)
_AdGenVoipUserProvBulkInstance_Type=Unsigned32
_AdGenVoipUserProvBulkInstance_Object=MibScalar
adGenVoipUserProvBulkInstance=_AdGenVoipUserProvBulkInstance_Object((1,3,6,1,4,1,664,5,70,20,1,5,4),_AdGenVoipUserProvBulkInstance_Type())
adGenVoipUserProvBulkInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipUserProvBulkInstance.setStatus(_A)
_AdGenVoipScalarProv_ObjectIdentity=ObjectIdentity
adGenVoipScalarProv=_AdGenVoipScalarProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,6))
class _AdGenVoipScalarFlashhookMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('interpreted',1),('transparent',2)))
_AdGenVoipScalarFlashhookMode_Type.__name__=_D
_AdGenVoipScalarFlashhookMode_Object=MibScalar
adGenVoipScalarFlashhookMode=_AdGenVoipScalarFlashhookMode_Object((1,3,6,1,4,1,664,5,70,20,1,6,1),_AdGenVoipScalarFlashhookMode_Type())
adGenVoipScalarFlashhookMode.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarFlashhookMode.setStatus(_A)
class _AdGenVoipScalarConferenceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_M,2)))
_AdGenVoipScalarConferenceMode_Type.__name__=_D
_AdGenVoipScalarConferenceMode_Object=MibScalar
adGenVoipScalarConferenceMode=_AdGenVoipScalarConferenceMode_Object((1,3,6,1,4,1,664,5,70,20,1,6,2),_AdGenVoipScalarConferenceMode_Type())
adGenVoipScalarConferenceMode.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarConferenceMode.setStatus(_A)
class _AdGenVoipScalarConfLocalOriginatorFlashhook_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('drop',1),(_o,2),('split',3)))
_AdGenVoipScalarConfLocalOriginatorFlashhook_Type.__name__=_D
_AdGenVoipScalarConfLocalOriginatorFlashhook_Object=MibScalar
adGenVoipScalarConfLocalOriginatorFlashhook=_AdGenVoipScalarConfLocalOriginatorFlashhook_Object((1,3,6,1,4,1,664,5,70,20,1,6,3),_AdGenVoipScalarConfLocalOriginatorFlashhook_Type())
adGenVoipScalarConfLocalOriginatorFlashhook.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarConfLocalOriginatorFlashhook.setStatus(_A)
class _AdGenVoipScalarConfLocalOriginatorOnhook_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('persist',1),('terminate',2)))
_AdGenVoipScalarConfLocalOriginatorOnhook_Type.__name__=_D
_AdGenVoipScalarConfLocalOriginatorOnhook_Object=MibScalar
adGenVoipScalarConfLocalOriginatorOnhook=_AdGenVoipScalarConfLocalOriginatorOnhook_Object((1,3,6,1,4,1,664,5,70,20,1,6,4),_AdGenVoipScalarConfLocalOriginatorOnhook_Type())
adGenVoipScalarConfLocalOriginatorOnhook.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarConfLocalOriginatorOnhook.setStatus(_A)
class _AdGenVoipScalarConfLocalPartyDisconnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('continue',1),('transfer',2)))
_AdGenVoipScalarConfLocalPartyDisconnect_Type.__name__=_D
_AdGenVoipScalarConfLocalPartyDisconnect_Object=MibScalar
adGenVoipScalarConfLocalPartyDisconnect=_AdGenVoipScalarConfLocalPartyDisconnect_Object((1,3,6,1,4,1,664,5,70,20,1,6,5),_AdGenVoipScalarConfLocalPartyDisconnect_Type())
adGenVoipScalarConfLocalPartyDisconnect.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarConfLocalPartyDisconnect.setStatus(_A)
class _AdGenVoipScalarRtpUdpOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1026,60000))
_AdGenVoipScalarRtpUdpOffset_Type.__name__=_D
_AdGenVoipScalarRtpUdpOffset_Object=MibScalar
adGenVoipScalarRtpUdpOffset=_AdGenVoipScalarRtpUdpOffset_Object((1,3,6,1,4,1,664,5,70,20,1,6,6),_AdGenVoipScalarRtpUdpOffset_Type())
adGenVoipScalarRtpUdpOffset.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarRtpUdpOffset.setStatus(_A)
class _AdGenVoipScalarSPREMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_M,2)))
_AdGenVoipScalarSPREMode_Type.__name__=_D
_AdGenVoipScalarSPREMode_Object=MibScalar
adGenVoipScalarSPREMode=_AdGenVoipScalarSPREMode_Object((1,3,6,1,4,1,664,5,70,20,1,6,7),_AdGenVoipScalarSPREMode_Type())
adGenVoipScalarSPREMode.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarSPREMode.setStatus(_A)
class _AdGenVoipScalarInterdigitTimer_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AdGenVoipScalarInterdigitTimer_Type.__name__=_D
_AdGenVoipScalarInterdigitTimer_Object=MibScalar
adGenVoipScalarInterdigitTimer=_AdGenVoipScalarInterdigitTimer_Object((1,3,6,1,4,1,664,5,70,20,1,6,8),_AdGenVoipScalarInterdigitTimer_Type())
adGenVoipScalarInterdigitTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarInterdigitTimer.setStatus(_A)
class _AdGenVoipScalarAlertingTimer_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AdGenVoipScalarAlertingTimer_Type.__name__=_D
_AdGenVoipScalarAlertingTimer_Object=MibScalar
adGenVoipScalarAlertingTimer=_AdGenVoipScalarAlertingTimer_Object((1,3,6,1,4,1,664,5,70,20,1,6,9),_AdGenVoipScalarAlertingTimer_Type())
adGenVoipScalarAlertingTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarAlertingTimer.setStatus(_A)
_AdGenVoipScalarTransferOnHangup_Type=TruthValue
_AdGenVoipScalarTransferOnHangup_Object=MibScalar
adGenVoipScalarTransferOnHangup=_AdGenVoipScalarTransferOnHangup_Object((1,3,6,1,4,1,664,5,70,20,1,6,10),_AdGenVoipScalarTransferOnHangup_Type())
adGenVoipScalarTransferOnHangup.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarTransferOnHangup.setStatus(_A)
class _AdGenVoipScalarFlashhookThreholdMin_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,1550))
_AdGenVoipScalarFlashhookThreholdMin_Type.__name__=_D
_AdGenVoipScalarFlashhookThreholdMin_Object=MibScalar
adGenVoipScalarFlashhookThreholdMin=_AdGenVoipScalarFlashhookThreholdMin_Object((1,3,6,1,4,1,664,5,70,20,1,6,11),_AdGenVoipScalarFlashhookThreholdMin_Type())
adGenVoipScalarFlashhookThreholdMin.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarFlashhookThreholdMin.setStatus(_A)
class _AdGenVoipScalarFlashhookThreholdMax_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,1550))
_AdGenVoipScalarFlashhookThreholdMax_Type.__name__=_D
_AdGenVoipScalarFlashhookThreholdMax_Object=MibScalar
adGenVoipScalarFlashhookThreholdMax=_AdGenVoipScalarFlashhookThreholdMax_Object((1,3,6,1,4,1,664,5,70,20,1,6,12),_AdGenVoipScalarFlashhookThreholdMax_Type())
adGenVoipScalarFlashhookThreholdMax.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarFlashhookThreholdMax.setStatus(_A)
class _AdGenVoipScalarEmergencyNumberInhibitOnHook_Type(TruthValue):defaultValue=2
_AdGenVoipScalarEmergencyNumberInhibitOnHook_Type.__name__=_K
_AdGenVoipScalarEmergencyNumberInhibitOnHook_Object=MibScalar
adGenVoipScalarEmergencyNumberInhibitOnHook=_AdGenVoipScalarEmergencyNumberInhibitOnHook_Object((1,3,6,1,4,1,664,5,70,20,1,6,13),_AdGenVoipScalarEmergencyNumberInhibitOnHook_Type())
adGenVoipScalarEmergencyNumberInhibitOnHook.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarEmergencyNumberInhibitOnHook.setStatus(_A)
class _AdGenVoipScalarEmergencyNumberRingingTimemout_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_AdGenVoipScalarEmergencyNumberRingingTimemout_Type.__name__=_D
_AdGenVoipScalarEmergencyNumberRingingTimemout_Object=MibScalar
adGenVoipScalarEmergencyNumberRingingTimemout=_AdGenVoipScalarEmergencyNumberRingingTimemout_Object((1,3,6,1,4,1,664,5,70,20,1,6,14),_AdGenVoipScalarEmergencyNumberRingingTimemout_Type())
adGenVoipScalarEmergencyNumberRingingTimemout.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarEmergencyNumberRingingTimemout.setStatus(_A)
class _AdGenVoipScalarDefaultSipTrunk_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_AdGenVoipScalarDefaultSipTrunk_Type.__name__=_G
_AdGenVoipScalarDefaultSipTrunk_Object=MibScalar
adGenVoipScalarDefaultSipTrunk=_AdGenVoipScalarDefaultSipTrunk_Object((1,3,6,1,4,1,664,5,70,20,1,6,15),_AdGenVoipScalarDefaultSipTrunk_Type())
adGenVoipScalarDefaultSipTrunk.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarDefaultSipTrunk.setStatus(_A)
class _AdGenVoipScalarConnectedTimer_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AdGenVoipScalarConnectedTimer_Type.__name__=_D
_AdGenVoipScalarConnectedTimer_Object=MibScalar
adGenVoipScalarConnectedTimer=_AdGenVoipScalarConnectedTimer_Object((1,3,6,1,4,1,664,5,70,20,1,6,16),_AdGenVoipScalarConnectedTimer_Type())
adGenVoipScalarConnectedTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarConnectedTimer.setStatus(_A)
_AdGenVoipSPREMapScalarProv_ObjectIdentity=ObjectIdentity
adGenVoipSPREMapScalarProv=_AdGenVoipSPREMapScalarProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,7))
class _AdGenVoipScalarSPREMapDisableCallWaiting_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,49))
_AdGenVoipScalarSPREMapDisableCallWaiting_Type.__name__=_G
_AdGenVoipScalarSPREMapDisableCallWaiting_Object=MibScalar
adGenVoipScalarSPREMapDisableCallWaiting=_AdGenVoipScalarSPREMapDisableCallWaiting_Object((1,3,6,1,4,1,664,5,70,20,1,7,1),_AdGenVoipScalarSPREMapDisableCallWaiting_Type())
adGenVoipScalarSPREMapDisableCallWaiting.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarSPREMapDisableCallWaiting.setStatus(_A)
class _AdGenVoipScalarSPREMapDNDDisableEnable_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,49))
_AdGenVoipScalarSPREMapDNDDisableEnable_Type.__name__=_G
_AdGenVoipScalarSPREMapDNDDisableEnable_Object=MibScalar
adGenVoipScalarSPREMapDNDDisableEnable=_AdGenVoipScalarSPREMapDNDDisableEnable_Object((1,3,6,1,4,1,664,5,70,20,1,7,2),_AdGenVoipScalarSPREMapDNDDisableEnable_Type())
adGenVoipScalarSPREMapDNDDisableEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarSPREMapDNDDisableEnable.setStatus(_A)
class _AdGenVoipScalarSPREMapBlockCallerID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,49))
_AdGenVoipScalarSPREMapBlockCallerID_Type.__name__=_G
_AdGenVoipScalarSPREMapBlockCallerID_Object=MibScalar
adGenVoipScalarSPREMapBlockCallerID=_AdGenVoipScalarSPREMapBlockCallerID_Object((1,3,6,1,4,1,664,5,70,20,1,7,3),_AdGenVoipScalarSPREMapBlockCallerID_Type())
adGenVoipScalarSPREMapBlockCallerID.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipScalarSPREMapBlockCallerID.setStatus(_A)
_AdGenVoipDialingProfileProv_ObjectIdentity=ObjectIdentity
adGenVoipDialingProfileProv=_AdGenVoipDialingProfileProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,8))
_AdGenVoipDialingProfileDialPlanProv_ObjectIdentity=ObjectIdentity
adGenVoipDialingProfileDialPlanProv=_AdGenVoipDialingProfileDialPlanProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,8,1))
_AdGenVoipDialingProfileDialPlanProvCurrentNumber_Type=Integer32
_AdGenVoipDialingProfileDialPlanProvCurrentNumber_Object=MibScalar
adGenVoipDialingProfileDialPlanProvCurrentNumber=_AdGenVoipDialingProfileDialPlanProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,20,1,8,1,1),_AdGenVoipDialingProfileDialPlanProvCurrentNumber_Type())
adGenVoipDialingProfileDialPlanProvCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileDialPlanProvCurrentNumber.setStatus(_A)
_AdGenVoipDialingProfileDialPlanProvLastCreateError_Type=DisplayString
_AdGenVoipDialingProfileDialPlanProvLastCreateError_Object=MibScalar
adGenVoipDialingProfileDialPlanProvLastCreateError=_AdGenVoipDialingProfileDialPlanProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,20,1,8,1,2),_AdGenVoipDialingProfileDialPlanProvLastCreateError_Type())
adGenVoipDialingProfileDialPlanProvLastCreateError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileDialPlanProvLastCreateError.setStatus(_A)
_AdGenVoipDialingProfileDialPlanProvTable_Object=MibTable
adGenVoipDialingProfileDialPlanProvTable=_AdGenVoipDialingProfileDialPlanProvTable_Object((1,3,6,1,4,1,664,5,70,20,1,8,1,3))
if mibBuilder.loadTexts:adGenVoipDialingProfileDialPlanProvTable.setStatus(_A)
_AdGenVoipDialingProfileDialPlanProvEntry_Object=MibTableRow
adGenVoipDialingProfileDialPlanProvEntry=_AdGenVoipDialingProfileDialPlanProvEntry_Object((1,3,6,1,4,1,664,5,70,20,1,8,1,3,1))
adGenVoipDialingProfileDialPlanProvEntry.setIndexNames((1,_F,_p))
if mibBuilder.loadTexts:adGenVoipDialingProfileDialPlanProvEntry.setStatus(_A)
class _AdGenVoipDialingProfileDialPlanPatternEntryIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,76))
_AdGenVoipDialingProfileDialPlanPatternEntryIndex_Type.__name__=_G
_AdGenVoipDialingProfileDialPlanPatternEntryIndex_Object=MibTableColumn
adGenVoipDialingProfileDialPlanPatternEntryIndex=_AdGenVoipDialingProfileDialPlanPatternEntryIndex_Object((1,3,6,1,4,1,664,5,70,20,1,8,1,3,1,1),_AdGenVoipDialingProfileDialPlanPatternEntryIndex_Type())
adGenVoipDialingProfileDialPlanPatternEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVoipDialingProfileDialPlanPatternEntryIndex.setStatus(_A)
_AdGenVoipDialingProfileDialPlanRowStatus_Type=RowStatus
_AdGenVoipDialingProfileDialPlanRowStatus_Object=MibTableColumn
adGenVoipDialingProfileDialPlanRowStatus=_AdGenVoipDialingProfileDialPlanRowStatus_Object((1,3,6,1,4,1,664,5,70,20,1,8,1,3,1,2),_AdGenVoipDialingProfileDialPlanRowStatus_Type())
adGenVoipDialingProfileDialPlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialingProfileDialPlanRowStatus.setStatus(_A)
_AdGenVoipDialingProfileDialPlanLastErrorString_Type=DisplayString
_AdGenVoipDialingProfileDialPlanLastErrorString_Object=MibTableColumn
adGenVoipDialingProfileDialPlanLastErrorString=_AdGenVoipDialingProfileDialPlanLastErrorString_Object((1,3,6,1,4,1,664,5,70,20,1,8,1,3,1,3),_AdGenVoipDialingProfileDialPlanLastErrorString_Type())
adGenVoipDialingProfileDialPlanLastErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileDialPlanLastErrorString.setStatus(_A)
class _AdGenVoipDialingProfileDialPlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_M,3),(_a,4),(_b,5),(_c,6),(_d,7),(_e,8),(_f,9),('user1',10),('user2',11),('user3',12)))
_AdGenVoipDialingProfileDialPlanType_Type.__name__=_D
_AdGenVoipDialingProfileDialPlanType_Object=MibTableColumn
adGenVoipDialingProfileDialPlanType=_AdGenVoipDialingProfileDialPlanType_Object((1,3,6,1,4,1,664,5,70,20,1,8,1,3,1,4),_AdGenVoipDialingProfileDialPlanType_Type())
adGenVoipDialingProfileDialPlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialingProfileDialPlanType.setStatus(_A)
class _AdGenVoipDialingProfileDialPlanEmergencyNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_AdGenVoipDialingProfileDialPlanEmergencyNumber_Type.__name__=_D
_AdGenVoipDialingProfileDialPlanEmergencyNumber_Object=MibTableColumn
adGenVoipDialingProfileDialPlanEmergencyNumber=_AdGenVoipDialingProfileDialPlanEmergencyNumber_Object((1,3,6,1,4,1,664,5,70,20,1,8,1,3,1,5),_AdGenVoipDialingProfileDialPlanEmergencyNumber_Type())
adGenVoipDialingProfileDialPlanEmergencyNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialingProfileDialPlanEmergencyNumber.setStatus(_A)
class _AdGenVoipDialingProfileDialPlanExternalLineCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3)))
_AdGenVoipDialingProfileDialPlanExternalLineCode_Type.__name__=_D
_AdGenVoipDialingProfileDialPlanExternalLineCode_Object=MibTableColumn
adGenVoipDialingProfileDialPlanExternalLineCode=_AdGenVoipDialingProfileDialPlanExternalLineCode_Object((1,3,6,1,4,1,664,5,70,20,1,8,1,3,1,6),_AdGenVoipDialingProfileDialPlanExternalLineCode_Type())
adGenVoipDialingProfileDialPlanExternalLineCode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialingProfileDialPlanExternalLineCode.setStatus(_A)
_AdGenVoipDialingProfileDialPlanPattern_Type=DisplayString
_AdGenVoipDialingProfileDialPlanPattern_Object=MibTableColumn
adGenVoipDialingProfileDialPlanPattern=_AdGenVoipDialingProfileDialPlanPattern_Object((1,3,6,1,4,1,664,5,70,20,1,8,1,3,1,7),_AdGenVoipDialingProfileDialPlanPattern_Type())
adGenVoipDialingProfileDialPlanPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileDialPlanPattern.setStatus(_A)
_AdGenVoipDialingProfileDialPlanDialingProfile_Type=AdGenVoipDialingProfileName
_AdGenVoipDialingProfileDialPlanDialingProfile_Object=MibTableColumn
adGenVoipDialingProfileDialPlanDialingProfile=_AdGenVoipDialingProfileDialPlanDialingProfile_Object((1,3,6,1,4,1,664,5,70,20,1,8,1,3,1,8),_AdGenVoipDialingProfileDialPlanDialingProfile_Type())
adGenVoipDialingProfileDialPlanDialingProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileDialPlanDialingProfile.setStatus(_A)
_AdGenVoipDialingProfileSPREPatternProv_ObjectIdentity=ObjectIdentity
adGenVoipDialingProfileSPREPatternProv=_AdGenVoipDialingProfileSPREPatternProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,8,2))
_AdGenVoipDialingProfileSPREPatternProvCurrentNumber_Type=Integer32
_AdGenVoipDialingProfileSPREPatternProvCurrentNumber_Object=MibScalar
adGenVoipDialingProfileSPREPatternProvCurrentNumber=_AdGenVoipDialingProfileSPREPatternProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,20,1,8,2,1),_AdGenVoipDialingProfileSPREPatternProvCurrentNumber_Type())
adGenVoipDialingProfileSPREPatternProvCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileSPREPatternProvCurrentNumber.setStatus(_A)
_AdGenVoipDialingProfileSPREPatternProvLastCreateError_Type=DisplayString
_AdGenVoipDialingProfileSPREPatternProvLastCreateError_Object=MibScalar
adGenVoipDialingProfileSPREPatternProvLastCreateError=_AdGenVoipDialingProfileSPREPatternProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,20,1,8,2,2),_AdGenVoipDialingProfileSPREPatternProvLastCreateError_Type())
adGenVoipDialingProfileSPREPatternProvLastCreateError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileSPREPatternProvLastCreateError.setStatus(_A)
_AdGenVoipDialingProfileSPREPatternProvTable_Object=MibTable
adGenVoipDialingProfileSPREPatternProvTable=_AdGenVoipDialingProfileSPREPatternProvTable_Object((1,3,6,1,4,1,664,5,70,20,1,8,2,3))
if mibBuilder.loadTexts:adGenVoipDialingProfileSPREPatternProvTable.setStatus(_A)
_AdGenVoipDialingProfileSPREPatternProvEntry_Object=MibTableRow
adGenVoipDialingProfileSPREPatternProvEntry=_AdGenVoipDialingProfileSPREPatternProvEntry_Object((1,3,6,1,4,1,664,5,70,20,1,8,2,3,1))
adGenVoipDialingProfileSPREPatternProvEntry.setIndexNames((1,_F,_q))
if mibBuilder.loadTexts:adGenVoipDialingProfileSPREPatternProvEntry.setStatus(_A)
class _AdGenVoipDialingProfileSPREPatternEntryIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,80))
_AdGenVoipDialingProfileSPREPatternEntryIndex_Type.__name__=_G
_AdGenVoipDialingProfileSPREPatternEntryIndex_Object=MibTableColumn
adGenVoipDialingProfileSPREPatternEntryIndex=_AdGenVoipDialingProfileSPREPatternEntryIndex_Object((1,3,6,1,4,1,664,5,70,20,1,8,2,3,1,1),_AdGenVoipDialingProfileSPREPatternEntryIndex_Type())
adGenVoipDialingProfileSPREPatternEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVoipDialingProfileSPREPatternEntryIndex.setStatus(_A)
_AdGenVoipDialingProfileSPREPatternRowStatus_Type=RowStatus
_AdGenVoipDialingProfileSPREPatternRowStatus_Object=MibTableColumn
adGenVoipDialingProfileSPREPatternRowStatus=_AdGenVoipDialingProfileSPREPatternRowStatus_Object((1,3,6,1,4,1,664,5,70,20,1,8,2,3,1,2),_AdGenVoipDialingProfileSPREPatternRowStatus_Type())
adGenVoipDialingProfileSPREPatternRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialingProfileSPREPatternRowStatus.setStatus(_A)
_AdGenVoipDialingProfileSPREPatternLastErrorString_Type=DisplayString
_AdGenVoipDialingProfileSPREPatternLastErrorString_Object=MibTableColumn
adGenVoipDialingProfileSPREPatternLastErrorString=_AdGenVoipDialingProfileSPREPatternLastErrorString_Object((1,3,6,1,4,1,664,5,70,20,1,8,2,3,1,3),_AdGenVoipDialingProfileSPREPatternLastErrorString_Type())
adGenVoipDialingProfileSPREPatternLastErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileSPREPatternLastErrorString.setStatus(_A)
class _AdGenVoipDialingProfileSPREPatternTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3)))
_AdGenVoipDialingProfileSPREPatternTone_Type.__name__=_D
_AdGenVoipDialingProfileSPREPatternTone_Object=MibTableColumn
adGenVoipDialingProfileSPREPatternTone=_AdGenVoipDialingProfileSPREPatternTone_Object((1,3,6,1,4,1,664,5,70,20,1,8,2,3,1,4),_AdGenVoipDialingProfileSPREPatternTone_Type())
adGenVoipDialingProfileSPREPatternTone.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialingProfileSPREPatternTone.setStatus(_A)
_AdGenVoipDialingProfileSPREPattern_Type=DisplayString
_AdGenVoipDialingProfileSPREPattern_Object=MibTableColumn
adGenVoipDialingProfileSPREPattern=_AdGenVoipDialingProfileSPREPattern_Object((1,3,6,1,4,1,664,5,70,20,1,8,2,3,1,5),_AdGenVoipDialingProfileSPREPattern_Type())
adGenVoipDialingProfileSPREPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileSPREPattern.setStatus(_A)
_AdGenVoipDialingProfileSPREPatternDialingProfile_Type=AdGenVoipDialingProfileName
_AdGenVoipDialingProfileSPREPatternDialingProfile_Object=MibTableColumn
adGenVoipDialingProfileSPREPatternDialingProfile=_AdGenVoipDialingProfileSPREPatternDialingProfile_Object((1,3,6,1,4,1,664,5,70,20,1,8,2,3,1,6),_AdGenVoipDialingProfileSPREPatternDialingProfile_Type())
adGenVoipDialingProfileSPREPatternDialingProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileSPREPatternDialingProfile.setStatus(_A)
_AdGenVoipDialingProfileExternalLineCodeProv_ObjectIdentity=ObjectIdentity
adGenVoipDialingProfileExternalLineCodeProv=_AdGenVoipDialingProfileExternalLineCodeProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,8,3))
_AdGenVoipDialingProfileExternalLineCodeProvCurrentNumber_Type=Integer32
_AdGenVoipDialingProfileExternalLineCodeProvCurrentNumber_Object=MibScalar
adGenVoipDialingProfileExternalLineCodeProvCurrentNumber=_AdGenVoipDialingProfileExternalLineCodeProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,20,1,8,3,1),_AdGenVoipDialingProfileExternalLineCodeProvCurrentNumber_Type())
adGenVoipDialingProfileExternalLineCodeProvCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileExternalLineCodeProvCurrentNumber.setStatus(_A)
_AdGenVoipDialingProfileExternalLineCodeProvLastCreateError_Type=DisplayString
_AdGenVoipDialingProfileExternalLineCodeProvLastCreateError_Object=MibScalar
adGenVoipDialingProfileExternalLineCodeProvLastCreateError=_AdGenVoipDialingProfileExternalLineCodeProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,20,1,8,3,2),_AdGenVoipDialingProfileExternalLineCodeProvLastCreateError_Type())
adGenVoipDialingProfileExternalLineCodeProvLastCreateError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileExternalLineCodeProvLastCreateError.setStatus(_A)
_AdGenVoipDialingProfileExternalLineCodeProvTable_Object=MibTable
adGenVoipDialingProfileExternalLineCodeProvTable=_AdGenVoipDialingProfileExternalLineCodeProvTable_Object((1,3,6,1,4,1,664,5,70,20,1,8,3,3))
if mibBuilder.loadTexts:adGenVoipDialingProfileExternalLineCodeProvTable.setStatus(_A)
_AdGenVoipDialingProfileExternalLineCodeProvEntry_Object=MibTableRow
adGenVoipDialingProfileExternalLineCodeProvEntry=_AdGenVoipDialingProfileExternalLineCodeProvEntry_Object((1,3,6,1,4,1,664,5,70,20,1,8,3,3,1))
adGenVoipDialingProfileExternalLineCodeProvEntry.setIndexNames((1,_F,_r))
if mibBuilder.loadTexts:adGenVoipDialingProfileExternalLineCodeProvEntry.setStatus(_A)
class _AdGenVoipDialingProfileExternalLineCodeEntryIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,80))
_AdGenVoipDialingProfileExternalLineCodeEntryIndex_Type.__name__=_G
_AdGenVoipDialingProfileExternalLineCodeEntryIndex_Object=MibTableColumn
adGenVoipDialingProfileExternalLineCodeEntryIndex=_AdGenVoipDialingProfileExternalLineCodeEntryIndex_Object((1,3,6,1,4,1,664,5,70,20,1,8,3,3,1,1),_AdGenVoipDialingProfileExternalLineCodeEntryIndex_Type())
adGenVoipDialingProfileExternalLineCodeEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVoipDialingProfileExternalLineCodeEntryIndex.setStatus(_A)
_AdGenVoipDialingProfileExternalLineCodeRowStatus_Type=RowStatus
_AdGenVoipDialingProfileExternalLineCodeRowStatus_Object=MibTableColumn
adGenVoipDialingProfileExternalLineCodeRowStatus=_AdGenVoipDialingProfileExternalLineCodeRowStatus_Object((1,3,6,1,4,1,664,5,70,20,1,8,3,3,1,2),_AdGenVoipDialingProfileExternalLineCodeRowStatus_Type())
adGenVoipDialingProfileExternalLineCodeRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialingProfileExternalLineCodeRowStatus.setStatus(_A)
_AdGenVoipDialingProfileExternalLineCodeLastErrorString_Type=DisplayString
_AdGenVoipDialingProfileExternalLineCodeLastErrorString_Object=MibTableColumn
adGenVoipDialingProfileExternalLineCodeLastErrorString=_AdGenVoipDialingProfileExternalLineCodeLastErrorString_Object((1,3,6,1,4,1,664,5,70,20,1,8,3,3,1,3),_AdGenVoipDialingProfileExternalLineCodeLastErrorString_Type())
adGenVoipDialingProfileExternalLineCodeLastErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileExternalLineCodeLastErrorString.setStatus(_A)
class _AdGenVoipDialingProfileExternalLineCodeTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3)))
_AdGenVoipDialingProfileExternalLineCodeTone_Type.__name__=_D
_AdGenVoipDialingProfileExternalLineCodeTone_Object=MibTableColumn
adGenVoipDialingProfileExternalLineCodeTone=_AdGenVoipDialingProfileExternalLineCodeTone_Object((1,3,6,1,4,1,664,5,70,20,1,8,3,3,1,4),_AdGenVoipDialingProfileExternalLineCodeTone_Type())
adGenVoipDialingProfileExternalLineCodeTone.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialingProfileExternalLineCodeTone.setStatus(_A)
_AdGenVoipDialingProfileExternalLineCodePattern_Type=DisplayString
_AdGenVoipDialingProfileExternalLineCodePattern_Object=MibTableColumn
adGenVoipDialingProfileExternalLineCodePattern=_AdGenVoipDialingProfileExternalLineCodePattern_Object((1,3,6,1,4,1,664,5,70,20,1,8,3,3,1,5),_AdGenVoipDialingProfileExternalLineCodePattern_Type())
adGenVoipDialingProfileExternalLineCodePattern.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileExternalLineCodePattern.setStatus(_A)
_AdGenVoipDialingProfileExternalLineCodeDialingProfile_Type=AdGenVoipDialingProfileName
_AdGenVoipDialingProfileExternalLineCodeDialingProfile_Object=MibTableColumn
adGenVoipDialingProfileExternalLineCodeDialingProfile=_AdGenVoipDialingProfileExternalLineCodeDialingProfile_Object((1,3,6,1,4,1,664,5,70,20,1,8,3,3,1,6),_AdGenVoipDialingProfileExternalLineCodeDialingProfile_Type())
adGenVoipDialingProfileExternalLineCodeDialingProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileExternalLineCodeDialingProfile.setStatus(_A)
_AdGenVoipDialingProfileProvExt_ObjectIdentity=ObjectIdentity
adGenVoipDialingProfileProvExt=_AdGenVoipDialingProfileProvExt_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,8,4))
_AdGenVoipDialingProfileProvExtTable_Object=MibTable
adGenVoipDialingProfileProvExtTable=_AdGenVoipDialingProfileProvExtTable_Object((1,3,6,1,4,1,664,5,70,20,1,8,4,1))
if mibBuilder.loadTexts:adGenVoipDialingProfileProvExtTable.setStatus(_N)
_AdGenVoipDialingProfileProvExtEntry_Object=MibTableRow
adGenVoipDialingProfileProvExtEntry=_AdGenVoipDialingProfileProvExtEntry_Object((1,3,6,1,4,1,664,5,70,20,1,8,4,1,1))
adGenVoipDialingProfileProvExtEntry.setIndexNames((1,_F,_s))
if mibBuilder.loadTexts:adGenVoipDialingProfileProvExtEntry.setStatus(_N)
_AdGenVoipDialingProfileProvExtEntryIndex_Type=AdGenVoipDialingProfileName
_AdGenVoipDialingProfileProvExtEntryIndex_Object=MibTableColumn
adGenVoipDialingProfileProvExtEntryIndex=_AdGenVoipDialingProfileProvExtEntryIndex_Object((1,3,6,1,4,1,664,5,70,20,1,8,4,1,1,1),_AdGenVoipDialingProfileProvExtEntryIndex_Type())
adGenVoipDialingProfileProvExtEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVoipDialingProfileProvExtEntryIndex.setStatus(_N)
_AdGenVoipDialingProfileProvExtNumVoiceUsers_Type=Unsigned32
_AdGenVoipDialingProfileProvExtNumVoiceUsers_Object=MibTableColumn
adGenVoipDialingProfileProvExtNumVoiceUsers=_AdGenVoipDialingProfileProvExtNumVoiceUsers_Object((1,3,6,1,4,1,664,5,70,20,1,8,4,1,1,2),_AdGenVoipDialingProfileProvExtNumVoiceUsers_Type())
adGenVoipDialingProfileProvExtNumVoiceUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileProvExtNumVoiceUsers.setStatus(_N)
class _AdGenVoipDialingProfileProvExtRemoveProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_t,1))
_AdGenVoipDialingProfileProvExtRemoveProfile_Type.__name__=_D
_AdGenVoipDialingProfileProvExtRemoveProfile_Object=MibTableColumn
adGenVoipDialingProfileProvExtRemoveProfile=_AdGenVoipDialingProfileProvExtRemoveProfile_Object((1,3,6,1,4,1,664,5,70,20,1,8,4,1,1,3),_AdGenVoipDialingProfileProvExtRemoveProfile_Type())
adGenVoipDialingProfileProvExtRemoveProfile.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipDialingProfileProvExtRemoveProfile.setStatus(_N)
_AdGenVoipDialingProfileCommonProv_ObjectIdentity=ObjectIdentity
adGenVoipDialingProfileCommonProv=_AdGenVoipDialingProfileCommonProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,8,5))
_AdGenVoipDialingProfileCommonProvCurrentNumber_Type=Integer32
_AdGenVoipDialingProfileCommonProvCurrentNumber_Object=MibScalar
adGenVoipDialingProfileCommonProvCurrentNumber=_AdGenVoipDialingProfileCommonProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,20,1,8,5,1),_AdGenVoipDialingProfileCommonProvCurrentNumber_Type())
adGenVoipDialingProfileCommonProvCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileCommonProvCurrentNumber.setStatus(_A)
_AdGenVoipDialingProfileCommonProvLastCreateError_Type=DisplayString
_AdGenVoipDialingProfileCommonProvLastCreateError_Object=MibScalar
adGenVoipDialingProfileCommonProvLastCreateError=_AdGenVoipDialingProfileCommonProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,20,1,8,5,2),_AdGenVoipDialingProfileCommonProvLastCreateError_Type())
adGenVoipDialingProfileCommonProvLastCreateError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileCommonProvLastCreateError.setStatus(_A)
_AdGenVoipDialingProfileCommonProvTable_Object=MibTable
adGenVoipDialingProfileCommonProvTable=_AdGenVoipDialingProfileCommonProvTable_Object((1,3,6,1,4,1,664,5,70,20,1,8,5,3))
if mibBuilder.loadTexts:adGenVoipDialingProfileCommonProvTable.setStatus(_A)
_AdGenVoipDialingProfileCommonProvEntry_Object=MibTableRow
adGenVoipDialingProfileCommonProvEntry=_AdGenVoipDialingProfileCommonProvEntry_Object((1,3,6,1,4,1,664,5,70,20,1,8,5,3,1))
adGenVoipDialingProfileCommonProvEntry.setIndexNames((1,_F,_u))
if mibBuilder.loadTexts:adGenVoipDialingProfileCommonProvEntry.setStatus(_A)
_AdGenVoipDialingProfileCommonProvEntryIndex_Type=AdGenVoipDialingProfileName
_AdGenVoipDialingProfileCommonProvEntryIndex_Object=MibTableColumn
adGenVoipDialingProfileCommonProvEntryIndex=_AdGenVoipDialingProfileCommonProvEntryIndex_Object((1,3,6,1,4,1,664,5,70,20,1,8,5,3,1,1),_AdGenVoipDialingProfileCommonProvEntryIndex_Type())
adGenVoipDialingProfileCommonProvEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVoipDialingProfileCommonProvEntryIndex.setStatus(_A)
_AdGenVoipDialingProfileCommonProvNumVoiceUsers_Type=Unsigned32
_AdGenVoipDialingProfileCommonProvNumVoiceUsers_Object=MibTableColumn
adGenVoipDialingProfileCommonProvNumVoiceUsers=_AdGenVoipDialingProfileCommonProvNumVoiceUsers_Object((1,3,6,1,4,1,664,5,70,20,1,8,5,3,1,2),_AdGenVoipDialingProfileCommonProvNumVoiceUsers_Type())
adGenVoipDialingProfileCommonProvNumVoiceUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileCommonProvNumVoiceUsers.setStatus(_A)
class _AdGenVoipDialingProfileCommonProvRemoveProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_t,1))
_AdGenVoipDialingProfileCommonProvRemoveProfile_Type.__name__=_D
_AdGenVoipDialingProfileCommonProvRemoveProfile_Object=MibTableColumn
adGenVoipDialingProfileCommonProvRemoveProfile=_AdGenVoipDialingProfileCommonProvRemoveProfile_Object((1,3,6,1,4,1,664,5,70,20,1,8,5,3,1,3),_AdGenVoipDialingProfileCommonProvRemoveProfile_Type())
adGenVoipDialingProfileCommonProvRemoveProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialingProfileCommonProvRemoveProfile.setStatus(_A)
class _AdGenVoipDialingProfileCommonProvDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AdGenVoipDialingProfileCommonProvDescription_Type.__name__=_G
_AdGenVoipDialingProfileCommonProvDescription_Object=MibTableColumn
adGenVoipDialingProfileCommonProvDescription=_AdGenVoipDialingProfileCommonProvDescription_Object((1,3,6,1,4,1,664,5,70,20,1,8,5,3,1,4),_AdGenVoipDialingProfileCommonProvDescription_Type())
adGenVoipDialingProfileCommonProvDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialingProfileCommonProvDescription.setStatus(_A)
_AdGenVoipDialingProfileCommonProvRowStatus_Type=RowStatus
_AdGenVoipDialingProfileCommonProvRowStatus_Object=MibTableColumn
adGenVoipDialingProfileCommonProvRowStatus=_AdGenVoipDialingProfileCommonProvRowStatus_Object((1,3,6,1,4,1,664,5,70,20,1,8,5,3,1,5),_AdGenVoipDialingProfileCommonProvRowStatus_Type())
adGenVoipDialingProfileCommonProvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipDialingProfileCommonProvRowStatus.setStatus(_A)
_AdGenVoipDialingProfileCommonProvLastErrorString_Type=DisplayString
_AdGenVoipDialingProfileCommonProvLastErrorString_Object=MibTableColumn
adGenVoipDialingProfileCommonProvLastErrorString=_AdGenVoipDialingProfileCommonProvLastErrorString_Object((1,3,6,1,4,1,664,5,70,20,1,8,5,3,1,6),_AdGenVoipDialingProfileCommonProvLastErrorString_Type())
adGenVoipDialingProfileCommonProvLastErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipDialingProfileCommonProvLastErrorString.setStatus(_A)
_AdGenVoipCodecProfileNameProv_ObjectIdentity=ObjectIdentity
adGenVoipCodecProfileNameProv=_AdGenVoipCodecProfileNameProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,9))
_AdGenVoipCodecProfileNameProvCurrentNumber_Type=Integer32
_AdGenVoipCodecProfileNameProvCurrentNumber_Object=MibScalar
adGenVoipCodecProfileNameProvCurrentNumber=_AdGenVoipCodecProfileNameProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,20,1,9,1),_AdGenVoipCodecProfileNameProvCurrentNumber_Type())
adGenVoipCodecProfileNameProvCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipCodecProfileNameProvCurrentNumber.setStatus(_A)
_AdGenVoipCodecProfileNameProvLastCreateError_Type=DisplayString
_AdGenVoipCodecProfileNameProvLastCreateError_Object=MibScalar
adGenVoipCodecProfileNameProvLastCreateError=_AdGenVoipCodecProfileNameProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,20,1,9,2),_AdGenVoipCodecProfileNameProvLastCreateError_Type())
adGenVoipCodecProfileNameProvLastCreateError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipCodecProfileNameProvLastCreateError.setStatus(_A)
_AdGenVoipCodecProfileNameProvTable_Object=MibTable
adGenVoipCodecProfileNameProvTable=_AdGenVoipCodecProfileNameProvTable_Object((1,3,6,1,4,1,664,5,70,20,1,9,3))
if mibBuilder.loadTexts:adGenVoipCodecProfileNameProvTable.setStatus(_A)
_AdGenVoipCodecProfileNameProvEntry_Object=MibTableRow
adGenVoipCodecProfileNameProvEntry=_AdGenVoipCodecProfileNameProvEntry_Object((1,3,6,1,4,1,664,5,70,20,1,9,3,1))
adGenVoipCodecProfileNameProvEntry.setIndexNames((1,_F,_T))
if mibBuilder.loadTexts:adGenVoipCodecProfileNameProvEntry.setStatus(_A)
_AdGenVoipCodecProfileNameProvIndex_Type=AdGenVoipCodecProfileName
_AdGenVoipCodecProfileNameProvIndex_Object=MibTableColumn
adGenVoipCodecProfileNameProvIndex=_AdGenVoipCodecProfileNameProvIndex_Object((1,3,6,1,4,1,664,5,70,20,1,9,3,1,1),_AdGenVoipCodecProfileNameProvIndex_Type())
adGenVoipCodecProfileNameProvIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVoipCodecProfileNameProvIndex.setStatus(_A)
_AdGenVoipCodecProfileNameProvRowStatus_Type=RowStatus
_AdGenVoipCodecProfileNameProvRowStatus_Object=MibTableColumn
adGenVoipCodecProfileNameProvRowStatus=_AdGenVoipCodecProfileNameProvRowStatus_Object((1,3,6,1,4,1,664,5,70,20,1,9,3,1,2),_AdGenVoipCodecProfileNameProvRowStatus_Type())
adGenVoipCodecProfileNameProvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCodecProfileNameProvRowStatus.setStatus(_A)
_AdGenVoipCodecProfileNameProvLastErrorString_Type=DisplayString
_AdGenVoipCodecProfileNameProvLastErrorString_Object=MibTableColumn
adGenVoipCodecProfileNameProvLastErrorString=_AdGenVoipCodecProfileNameProvLastErrorString_Object((1,3,6,1,4,1,664,5,70,20,1,9,3,1,3),_AdGenVoipCodecProfileNameProvLastErrorString_Type())
adGenVoipCodecProfileNameProvLastErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipCodecProfileNameProvLastErrorString.setStatus(_A)
_AdGenVoipCodecProfilePreferenceLastCreateError_Type=DisplayString
_AdGenVoipCodecProfilePreferenceLastCreateError_Object=MibTableColumn
adGenVoipCodecProfilePreferenceLastCreateError=_AdGenVoipCodecProfilePreferenceLastCreateError_Object((1,3,6,1,4,1,664,5,70,20,1,9,3,1,4),_AdGenVoipCodecProfilePreferenceLastCreateError_Type())
adGenVoipCodecProfilePreferenceLastCreateError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipCodecProfilePreferenceLastCreateError.setStatus(_A)
_AdGenVoipCodecProfileProv_ObjectIdentity=ObjectIdentity
adGenVoipCodecProfileProv=_AdGenVoipCodecProfileProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,10))
_AdGenVoipCodecProfileProvTable_Object=MibTable
adGenVoipCodecProfileProvTable=_AdGenVoipCodecProfileProvTable_Object((1,3,6,1,4,1,664,5,70,20,1,10,1))
if mibBuilder.loadTexts:adGenVoipCodecProfileProvTable.setStatus(_A)
_AdGenVoipCodecProfileProvEntry_Object=MibTableRow
adGenVoipCodecProfileProvEntry=_AdGenVoipCodecProfileProvEntry_Object((1,3,6,1,4,1,664,5,70,20,1,10,1,1))
adGenVoipCodecProfileProvEntry.setIndexNames((0,_F,_T),(0,_F,_v))
if mibBuilder.loadTexts:adGenVoipCodecProfileProvEntry.setStatus(_A)
_AdGenVoipCodecProfileProvIndex_Type=Unsigned32
_AdGenVoipCodecProfileProvIndex_Object=MibTableColumn
adGenVoipCodecProfileProvIndex=_AdGenVoipCodecProfileProvIndex_Object((1,3,6,1,4,1,664,5,70,20,1,10,1,1,1),_AdGenVoipCodecProfileProvIndex_Type())
adGenVoipCodecProfileProvIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVoipCodecProfileProvIndex.setStatus(_A)
_AdGenVoipCodecProfileProvRowStatus_Type=RowStatus
_AdGenVoipCodecProfileProvRowStatus_Object=MibTableColumn
adGenVoipCodecProfileProvRowStatus=_AdGenVoipCodecProfileProvRowStatus_Object((1,3,6,1,4,1,664,5,70,20,1,10,1,1,2),_AdGenVoipCodecProfileProvRowStatus_Type())
adGenVoipCodecProfileProvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCodecProfileProvRowStatus.setStatus(_A)
_AdGenVoipCodecProfileProvLastErrorString_Type=DisplayString
_AdGenVoipCodecProfileProvLastErrorString_Object=MibTableColumn
adGenVoipCodecProfileProvLastErrorString=_AdGenVoipCodecProfileProvLastErrorString_Object((1,3,6,1,4,1,664,5,70,20,1,10,1,1,3),_AdGenVoipCodecProfileProvLastErrorString_Type())
adGenVoipCodecProfileProvLastErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipCodecProfileProvLastErrorString.setStatus(_A)
class _AdGenVoipCodecProfileProvPreference_Type(AdGenVoipCodecProfileType):defaultValue=1
_AdGenVoipCodecProfileProvPreference_Type.__name__=_w
_AdGenVoipCodecProfileProvPreference_Object=MibTableColumn
adGenVoipCodecProfileProvPreference=_AdGenVoipCodecProfileProvPreference_Object((1,3,6,1,4,1,664,5,70,20,1,10,1,1,4),_AdGenVoipCodecProfileProvPreference_Type())
adGenVoipCodecProfileProvPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCodecProfileProvPreference.setStatus(_A)
_AdGenVoipMediaProfileProv_ObjectIdentity=ObjectIdentity
adGenVoipMediaProfileProv=_AdGenVoipMediaProfileProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,11))
_AdGenVoipMediaProfileProvCurrentNumber_Type=Integer32
_AdGenVoipMediaProfileProvCurrentNumber_Object=MibScalar
adGenVoipMediaProfileProvCurrentNumber=_AdGenVoipMediaProfileProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,20,1,11,1),_AdGenVoipMediaProfileProvCurrentNumber_Type())
adGenVoipMediaProfileProvCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvCurrentNumber.setStatus(_A)
_AdGenVoipMediaProfileProvLastCreateError_Type=DisplayString
_AdGenVoipMediaProfileProvLastCreateError_Object=MibScalar
adGenVoipMediaProfileProvLastCreateError=_AdGenVoipMediaProfileProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,20,1,11,2),_AdGenVoipMediaProfileProvLastCreateError_Type())
adGenVoipMediaProfileProvLastCreateError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvLastCreateError.setStatus(_A)
_AdGenVoipMediaProfileProvTable_Object=MibTable
adGenVoipMediaProfileProvTable=_AdGenVoipMediaProfileProvTable_Object((1,3,6,1,4,1,664,5,70,20,1,11,3))
if mibBuilder.loadTexts:adGenVoipMediaProfileProvTable.setStatus(_A)
_AdGenVoipMediaProfileProvEntry_Object=MibTableRow
adGenVoipMediaProfileProvEntry=_AdGenVoipMediaProfileProvEntry_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1))
adGenVoipMediaProfileProvEntry.setIndexNames((1,_F,_x))
if mibBuilder.loadTexts:adGenVoipMediaProfileProvEntry.setStatus(_A)
_AdGenVoipMediaProfileProvEntryIndex_Type=AdGenVoipMediaProfileName
_AdGenVoipMediaProfileProvEntryIndex_Object=MibTableColumn
adGenVoipMediaProfileProvEntryIndex=_AdGenVoipMediaProfileProvEntryIndex_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,1),_AdGenVoipMediaProfileProvEntryIndex_Type())
adGenVoipMediaProfileProvEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvEntryIndex.setStatus(_A)
_AdGenVoipMediaProfileProvRowStatus_Type=RowStatus
_AdGenVoipMediaProfileProvRowStatus_Object=MibTableColumn
adGenVoipMediaProfileProvRowStatus=_AdGenVoipMediaProfileProvRowStatus_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,2),_AdGenVoipMediaProfileProvRowStatus_Type())
adGenVoipMediaProfileProvRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvRowStatus.setStatus(_A)
_AdGenVoipMediaProfileProvLastErrorString_Type=DisplayString
_AdGenVoipMediaProfileProvLastErrorString_Object=MibTableColumn
adGenVoipMediaProfileProvLastErrorString=_AdGenVoipMediaProfileProvLastErrorString_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,3),_AdGenVoipMediaProfileProvLastErrorString_Type())
adGenVoipMediaProfileProvLastErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvLastErrorString.setStatus(_A)
class _AdGenVoipMediaProfileProvRtpFramePktization_Type(Unsigned32):defaultValue=10
_AdGenVoipMediaProfileProvRtpFramePktization_Type.__name__=_I
_AdGenVoipMediaProfileProvRtpFramePktization_Object=MibTableColumn
adGenVoipMediaProfileProvRtpFramePktization=_AdGenVoipMediaProfileProvRtpFramePktization_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,4),_AdGenVoipMediaProfileProvRtpFramePktization_Type())
adGenVoipMediaProfileProvRtpFramePktization.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvRtpFramePktization.setStatus(_A)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvRtpFramePktization.setUnits(_O)
class _AdGenVoipMediaProfileProvRtpPktDelayNominal_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_AdGenVoipMediaProfileProvRtpPktDelayNominal_Type.__name__=_I
_AdGenVoipMediaProfileProvRtpPktDelayNominal_Object=MibTableColumn
adGenVoipMediaProfileProvRtpPktDelayNominal=_AdGenVoipMediaProfileProvRtpPktDelayNominal_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,5),_AdGenVoipMediaProfileProvRtpPktDelayNominal_Type())
adGenVoipMediaProfileProvRtpPktDelayNominal.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvRtpPktDelayNominal.setStatus(_A)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvRtpPktDelayNominal.setUnits(_O)
class _AdGenVoipMediaProfileProvRtpPktDelayMaximum_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,320))
_AdGenVoipMediaProfileProvRtpPktDelayMaximum_Type.__name__=_I
_AdGenVoipMediaProfileProvRtpPktDelayMaximum_Object=MibTableColumn
adGenVoipMediaProfileProvRtpPktDelayMaximum=_AdGenVoipMediaProfileProvRtpPktDelayMaximum_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,6),_AdGenVoipMediaProfileProvRtpPktDelayMaximum_Type())
adGenVoipMediaProfileProvRtpPktDelayMaximum.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvRtpPktDelayMaximum.setStatus(_A)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvRtpPktDelayMaximum.setUnits(_O)
class _AdGenVoipMediaProfileProvRtpDtmfRelay_Type(Unsigned32):defaultValue=2
_AdGenVoipMediaProfileProvRtpDtmfRelay_Type.__name__=_I
_AdGenVoipMediaProfileProvRtpDtmfRelay_Object=MibTableColumn
adGenVoipMediaProfileProvRtpDtmfRelay=_AdGenVoipMediaProfileProvRtpDtmfRelay_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,7),_AdGenVoipMediaProfileProvRtpDtmfRelay_Type())
adGenVoipMediaProfileProvRtpDtmfRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvRtpDtmfRelay.setStatus(_A)
class _AdGenVoipMediaProfileProvRtpQosDscp_Type(Unsigned32):defaultValue=46;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AdGenVoipMediaProfileProvRtpQosDscp_Type.__name__=_I
_AdGenVoipMediaProfileProvRtpQosDscp_Object=MibTableColumn
adGenVoipMediaProfileProvRtpQosDscp=_AdGenVoipMediaProfileProvRtpQosDscp_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,8),_AdGenVoipMediaProfileProvRtpQosDscp_Type())
adGenVoipMediaProfileProvRtpQosDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvRtpQosDscp.setStatus(_A)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvRtpQosDscp.setUnits('priority')
class _AdGenVoipMediaProfileProvRtpLocalPortMin_Type(Unsigned32):defaultValue=10000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1026,60000))
_AdGenVoipMediaProfileProvRtpLocalPortMin_Type.__name__=_I
_AdGenVoipMediaProfileProvRtpLocalPortMin_Object=MibTableColumn
adGenVoipMediaProfileProvRtpLocalPortMin=_AdGenVoipMediaProfileProvRtpLocalPortMin_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,9),_AdGenVoipMediaProfileProvRtpLocalPortMin_Type())
adGenVoipMediaProfileProvRtpLocalPortMin.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvRtpLocalPortMin.setStatus(_A)
class _AdGenVoipMediaProfileProvRtpLocalPortMax_Type(Unsigned32):defaultValue=60000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1026,60000))
_AdGenVoipMediaProfileProvRtpLocalPortMax_Type.__name__=_I
_AdGenVoipMediaProfileProvRtpLocalPortMax_Object=MibTableColumn
adGenVoipMediaProfileProvRtpLocalPortMax=_AdGenVoipMediaProfileProvRtpLocalPortMax_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,10),_AdGenVoipMediaProfileProvRtpLocalPortMax_Type())
adGenVoipMediaProfileProvRtpLocalPortMax.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvRtpLocalPortMax.setStatus(_A)
class _AdGenVoipMediaProfileProvFaxMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('modemPassThrough',1),('t38',2)))
_AdGenVoipMediaProfileProvFaxMode_Type.__name__=_D
_AdGenVoipMediaProfileProvFaxMode_Object=MibTableColumn
adGenVoipMediaProfileProvFaxMode=_AdGenVoipMediaProfileProvFaxMode_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,11),_AdGenVoipMediaProfileProvFaxMode_Type())
adGenVoipMediaProfileProvFaxMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvFaxMode.setStatus(_A)
class _AdGenVoipMediaProfileProvEchoCancellation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_L,2)))
_AdGenVoipMediaProfileProvEchoCancellation_Type.__name__=_D
_AdGenVoipMediaProfileProvEchoCancellation_Object=MibTableColumn
adGenVoipMediaProfileProvEchoCancellation=_AdGenVoipMediaProfileProvEchoCancellation_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,12),_AdGenVoipMediaProfileProvEchoCancellation_Type())
adGenVoipMediaProfileProvEchoCancellation.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvEchoCancellation.setStatus(_A)
class _AdGenVoipMediaProfileProvFlashHookMin_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,1550))
_AdGenVoipMediaProfileProvFlashHookMin_Type.__name__=_I
_AdGenVoipMediaProfileProvFlashHookMin_Object=MibTableColumn
adGenVoipMediaProfileProvFlashHookMin=_AdGenVoipMediaProfileProvFlashHookMin_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,13),_AdGenVoipMediaProfileProvFlashHookMin_Type())
adGenVoipMediaProfileProvFlashHookMin.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvFlashHookMin.setStatus(_A)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvFlashHookMin.setUnits(_O)
class _AdGenVoipMediaProfileProvFlashHookMax_Type(Unsigned32):defaultValue=1000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,1550))
_AdGenVoipMediaProfileProvFlashHookMax_Type.__name__=_I
_AdGenVoipMediaProfileProvFlashHookMax_Object=MibTableColumn
adGenVoipMediaProfileProvFlashHookMax=_AdGenVoipMediaProfileProvFlashHookMax_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,14),_AdGenVoipMediaProfileProvFlashHookMax_Type())
adGenVoipMediaProfileProvFlashHookMax.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvFlashHookMax.setStatus(_A)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvFlashHookMax.setUnits(_O)
class _AdGenVoipMediaProfileProvVAD_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_L,2)))
_AdGenVoipMediaProfileProvVAD_Type.__name__=_D
_AdGenVoipMediaProfileProvVAD_Object=MibTableColumn
adGenVoipMediaProfileProvVAD=_AdGenVoipMediaProfileProvVAD_Object((1,3,6,1,4,1,664,5,70,20,1,11,3,1,15),_AdGenVoipMediaProfileProvVAD_Type())
adGenVoipMediaProfileProvVAD.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipMediaProfileProvVAD.setStatus(_A)
_AdGenVoipCallFeatureProfileProv_ObjectIdentity=ObjectIdentity
adGenVoipCallFeatureProfileProv=_AdGenVoipCallFeatureProfileProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,12))
_AdGenVoipCallFeatureProfileCurrentNumber_Type=Integer32
_AdGenVoipCallFeatureProfileCurrentNumber_Object=MibScalar
adGenVoipCallFeatureProfileCurrentNumber=_AdGenVoipCallFeatureProfileCurrentNumber_Object((1,3,6,1,4,1,664,5,70,20,1,12,1),_AdGenVoipCallFeatureProfileCurrentNumber_Type())
adGenVoipCallFeatureProfileCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileCurrentNumber.setStatus(_A)
_AdGenVoipCallFeatureProfileLastCreateError_Type=DisplayString
_AdGenVoipCallFeatureProfileLastCreateError_Object=MibScalar
adGenVoipCallFeatureProfileLastCreateError=_AdGenVoipCallFeatureProfileLastCreateError_Object((1,3,6,1,4,1,664,5,70,20,1,12,2),_AdGenVoipCallFeatureProfileLastCreateError_Type())
adGenVoipCallFeatureProfileLastCreateError.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileLastCreateError.setStatus(_A)
_AdGenVoipCallFeatureProfileProvTable_Object=MibTable
adGenVoipCallFeatureProfileProvTable=_AdGenVoipCallFeatureProfileProvTable_Object((1,3,6,1,4,1,664,5,70,20,1,12,3))
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileProvTable.setStatus(_A)
_AdGenVoipCallFeatureProfileProvEntry_Object=MibTableRow
adGenVoipCallFeatureProfileProvEntry=_AdGenVoipCallFeatureProfileProvEntry_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1))
adGenVoipCallFeatureProfileProvEntry.setIndexNames((1,_F,_y))
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileProvEntry.setStatus(_A)
_AdGenVoipCallFeatureProfileEntryIndex_Type=AdGenVoipCallFeatureProfileName
_AdGenVoipCallFeatureProfileEntryIndex_Object=MibTableColumn
adGenVoipCallFeatureProfileEntryIndex=_AdGenVoipCallFeatureProfileEntryIndex_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1,1),_AdGenVoipCallFeatureProfileEntryIndex_Type())
adGenVoipCallFeatureProfileEntryIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileEntryIndex.setStatus(_A)
_AdGenVoipCallFeatureProfileRowStatus_Type=RowStatus
_AdGenVoipCallFeatureProfileRowStatus_Object=MibTableColumn
adGenVoipCallFeatureProfileRowStatus=_AdGenVoipCallFeatureProfileRowStatus_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1,2),_AdGenVoipCallFeatureProfileRowStatus_Type())
adGenVoipCallFeatureProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileRowStatus.setStatus(_A)
_AdGenVoipCallFeatureProfileLastErrorString_Type=DisplayString
_AdGenVoipCallFeatureProfileLastErrorString_Object=MibTableColumn
adGenVoipCallFeatureProfileLastErrorString=_AdGenVoipCallFeatureProfileLastErrorString_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1,3),_AdGenVoipCallFeatureProfileLastErrorString_Type())
adGenVoipCallFeatureProfileLastErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileLastErrorString.setStatus(_A)
class _AdGenVoipCallFeatureProfileEmergencyNumberRingingTimeout_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_AdGenVoipCallFeatureProfileEmergencyNumberRingingTimeout_Type.__name__=_D
_AdGenVoipCallFeatureProfileEmergencyNumberRingingTimeout_Object=MibTableColumn
adGenVoipCallFeatureProfileEmergencyNumberRingingTimeout=_AdGenVoipCallFeatureProfileEmergencyNumberRingingTimeout_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1,4),_AdGenVoipCallFeatureProfileEmergencyNumberRingingTimeout_Type())
adGenVoipCallFeatureProfileEmergencyNumberRingingTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileEmergencyNumberRingingTimeout.setStatus(_A)
class _AdGenVoipCallFeatureProfileEmergencyNumberOnhook_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inhibit',1),('allow',2)))
_AdGenVoipCallFeatureProfileEmergencyNumberOnhook_Type.__name__=_D
_AdGenVoipCallFeatureProfileEmergencyNumberOnhook_Object=MibTableColumn
adGenVoipCallFeatureProfileEmergencyNumberOnhook=_AdGenVoipCallFeatureProfileEmergencyNumberOnhook_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1,5),_AdGenVoipCallFeatureProfileEmergencyNumberOnhook_Type())
adGenVoipCallFeatureProfileEmergencyNumberOnhook.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileEmergencyNumberOnhook.setStatus(_A)
class _AdGenVoipCallFeatureProfileCallWaiting_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_J,2)))
_AdGenVoipCallFeatureProfileCallWaiting_Type.__name__=_D
_AdGenVoipCallFeatureProfileCallWaiting_Object=MibTableColumn
adGenVoipCallFeatureProfileCallWaiting=_AdGenVoipCallFeatureProfileCallWaiting_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1,6),_AdGenVoipCallFeatureProfileCallWaiting_Type())
adGenVoipCallFeatureProfileCallWaiting.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileCallWaiting.setStatus(_A)
class _AdGenVoipCallFeatureProfileCallerIdInbound_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_J,2)))
_AdGenVoipCallFeatureProfileCallerIdInbound_Type.__name__=_D
_AdGenVoipCallFeatureProfileCallerIdInbound_Object=MibTableColumn
adGenVoipCallFeatureProfileCallerIdInbound=_AdGenVoipCallFeatureProfileCallerIdInbound_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1,7),_AdGenVoipCallFeatureProfileCallerIdInbound_Type())
adGenVoipCallFeatureProfileCallerIdInbound.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileCallerIdInbound.setStatus(_A)
class _AdGenVoipCallFeatureProfileCallerIdOutbound_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_J,2)))
_AdGenVoipCallFeatureProfileCallerIdOutbound_Type.__name__=_D
_AdGenVoipCallFeatureProfileCallerIdOutbound_Object=MibTableColumn
adGenVoipCallFeatureProfileCallerIdOutbound=_AdGenVoipCallFeatureProfileCallerIdOutbound_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1,8),_AdGenVoipCallFeatureProfileCallerIdOutbound_Type())
adGenVoipCallFeatureProfileCallerIdOutbound.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileCallerIdOutbound.setStatus(_A)
class _AdGenVoipCallFeatureProfileTransferOnHangup_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_J,2)))
_AdGenVoipCallFeatureProfileTransferOnHangup_Type.__name__=_D
_AdGenVoipCallFeatureProfileTransferOnHangup_Object=MibTableColumn
adGenVoipCallFeatureProfileTransferOnHangup=_AdGenVoipCallFeatureProfileTransferOnHangup_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1,9),_AdGenVoipCallFeatureProfileTransferOnHangup_Type())
adGenVoipCallFeatureProfileTransferOnHangup.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileTransferOnHangup.setStatus(_A)
class _AdGenVoipCallFeatureProfileTimeoutAlerting_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AdGenVoipCallFeatureProfileTimeoutAlerting_Type.__name__=_D
_AdGenVoipCallFeatureProfileTimeoutAlerting_Object=MibTableColumn
adGenVoipCallFeatureProfileTimeoutAlerting=_AdGenVoipCallFeatureProfileTimeoutAlerting_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1,10),_AdGenVoipCallFeatureProfileTimeoutAlerting_Type())
adGenVoipCallFeatureProfileTimeoutAlerting.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileTimeoutAlerting.setStatus(_A)
class _AdGenVoipCallFeatureProfileTimeoutInterdigit_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AdGenVoipCallFeatureProfileTimeoutInterdigit_Type.__name__=_D
_AdGenVoipCallFeatureProfileTimeoutInterdigit_Object=MibTableColumn
adGenVoipCallFeatureProfileTimeoutInterdigit=_AdGenVoipCallFeatureProfileTimeoutInterdigit_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1,11),_AdGenVoipCallFeatureProfileTimeoutInterdigit_Type())
adGenVoipCallFeatureProfileTimeoutInterdigit.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileTimeoutInterdigit.setStatus(_A)
class _AdGenVoipCallFeatureProfileConference_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),(_J,2)))
_AdGenVoipCallFeatureProfileConference_Type.__name__=_D
_AdGenVoipCallFeatureProfileConference_Object=MibTableColumn
adGenVoipCallFeatureProfileConference=_AdGenVoipCallFeatureProfileConference_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1,12),_AdGenVoipCallFeatureProfileConference_Type())
adGenVoipCallFeatureProfileConference.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileConference.setStatus(_A)
class _AdGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('drop',1),(_o,2),('split',3)))
_AdGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook_Type.__name__=_D
_AdGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook_Object=MibTableColumn
adGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook=_AdGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1,13),_AdGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook_Type())
adGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook.setStatus(_A)
class _AdGenVoipCallFeatureProfileFeatureMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_M,2)))
_AdGenVoipCallFeatureProfileFeatureMode_Type.__name__=_D
_AdGenVoipCallFeatureProfileFeatureMode_Object=MibTableColumn
adGenVoipCallFeatureProfileFeatureMode=_AdGenVoipCallFeatureProfileFeatureMode_Object((1,3,6,1,4,1,664,5,70,20,1,12,3,1,14),_AdGenVoipCallFeatureProfileFeatureMode_Type())
adGenVoipCallFeatureProfileFeatureMode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenVoipCallFeatureProfileFeatureMode.setStatus(_A)
_AdGenVoipUserReverseLookup_ObjectIdentity=ObjectIdentity
adGenVoipUserReverseLookup=_AdGenVoipUserReverseLookup_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,13))
_AdGenVoipUserReverseLookupTable_Object=MibTable
adGenVoipUserReverseLookupTable=_AdGenVoipUserReverseLookupTable_Object((1,3,6,1,4,1,664,5,70,20,1,13,1))
if mibBuilder.loadTexts:adGenVoipUserReverseLookupTable.setStatus(_A)
_AdGenVoipUserReverseLookupTableEntry_Object=MibTableRow
adGenVoipUserReverseLookupTableEntry=_AdGenVoipUserReverseLookupTableEntry_Object((1,3,6,1,4,1,664,5,70,20,1,13,1,1))
adGenVoipUserReverseLookupTableEntry.setIndexNames((0,_F,_z))
if mibBuilder.loadTexts:adGenVoipUserReverseLookupTableEntry.setStatus(_A)
_AdGenVoipUserReverseLookupTableEntryIndex_Type=AdGenVoipCallReverseLookupIfIndex
_AdGenVoipUserReverseLookupTableEntryIndex_Object=MibTableColumn
adGenVoipUserReverseLookupTableEntryIndex=_AdGenVoipUserReverseLookupTableEntryIndex_Object((1,3,6,1,4,1,664,5,70,20,1,13,1,1,1),_AdGenVoipUserReverseLookupTableEntryIndex_Type())
adGenVoipUserReverseLookupTableEntryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipUserReverseLookupTableEntryIndex.setStatus(_A)
_AdGenVoipUserReverseLookupTableUserName_Type=DisplayString
_AdGenVoipUserReverseLookupTableUserName_Object=MibTableColumn
adGenVoipUserReverseLookupTableUserName=_AdGenVoipUserReverseLookupTableUserName_Object((1,3,6,1,4,1,664,5,70,20,1,13,1,1,2),_AdGenVoipUserReverseLookupTableUserName_Type())
adGenVoipUserReverseLookupTableUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipUserReverseLookupTableUserName.setStatus(_A)
_AdGenVoipSDPProv_ObjectIdentity=ObjectIdentity
adGenVoipSDPProv=_AdGenVoipSDPProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,1,14))
class _AdGenVoipSDPGrammarPtime_Type(TruthValue):defaultValue=2
_AdGenVoipSDPGrammarPtime_Type.__name__=_K
_AdGenVoipSDPGrammarPtime_Object=MibScalar
adGenVoipSDPGrammarPtime=_AdGenVoipSDPGrammarPtime_Object((1,3,6,1,4,1,664,5,70,20,1,14,1),_AdGenVoipSDPGrammarPtime_Type())
adGenVoipSDPGrammarPtime.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipSDPGrammarPtime.setStatus(_A)
class _AdGenVoipSDPGrammarSuppressSilenceSupp_Type(TruthValue):defaultValue=2
_AdGenVoipSDPGrammarSuppressSilenceSupp_Type.__name__=_K
_AdGenVoipSDPGrammarSuppressSilenceSupp_Object=MibScalar
adGenVoipSDPGrammarSuppressSilenceSupp=_AdGenVoipSDPGrammarSuppressSilenceSupp_Object((1,3,6,1,4,1,664,5,70,20,1,14,2),_AdGenVoipSDPGrammarSuppressSilenceSupp_Type())
adGenVoipSDPGrammarSuppressSilenceSupp.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenVoipSDPGrammarSuppressSilenceSupp.setStatus(_A)
_AdGenVoipStatus_ObjectIdentity=ObjectIdentity
adGenVoipStatus=_AdGenVoipStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,2))
_AdGenVoipUserStatus_ObjectIdentity=ObjectIdentity
adGenVoipUserStatus=_AdGenVoipUserStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,2,1))
_AdGenVoipUserHotlineStatus_ObjectIdentity=ObjectIdentity
adGenVoipUserHotlineStatus=_AdGenVoipUserHotlineStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,2,1,1))
_AdGenVoipUserHotlineStatusTable_Object=MibTable
adGenVoipUserHotlineStatusTable=_AdGenVoipUserHotlineStatusTable_Object((1,3,6,1,4,1,664,5,70,20,2,1,1,1))
if mibBuilder.loadTexts:adGenVoipUserHotlineStatusTable.setStatus(_A)
_AdGenVoipUserHotlineStatusTableEntry_Object=MibTableRow
adGenVoipUserHotlineStatusTableEntry=_AdGenVoipUserHotlineStatusTableEntry_Object((1,3,6,1,4,1,664,5,70,20,2,1,1,1,1))
adGenVoipUserHotlineStatusTableEntry.setIndexNames((0,_U,_V),(0,_F,_A0))
if mibBuilder.loadTexts:adGenVoipUserHotlineStatusTableEntry.setStatus(_A)
_AdGenVoipUserHotlineStatusEntryIndex_Type=AdGenVoipUserNumber
_AdGenVoipUserHotlineStatusEntryIndex_Object=MibTableColumn
adGenVoipUserHotlineStatusEntryIndex=_AdGenVoipUserHotlineStatusEntryIndex_Object((1,3,6,1,4,1,664,5,70,20,2,1,1,1,1,1),_AdGenVoipUserHotlineStatusEntryIndex_Type())
adGenVoipUserHotlineStatusEntryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipUserHotlineStatusEntryIndex.setStatus(_A)
class _AdGenVoipUserHotlineStatusNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_AdGenVoipUserHotlineStatusNumber_Type.__name__=_G
_AdGenVoipUserHotlineStatusNumber_Object=MibTableColumn
adGenVoipUserHotlineStatusNumber=_AdGenVoipUserHotlineStatusNumber_Object((1,3,6,1,4,1,664,5,70,20,2,1,1,1,1,2),_AdGenVoipUserHotlineStatusNumber_Type())
adGenVoipUserHotlineStatusNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipUserHotlineStatusNumber.setStatus(_A)
_AdGenVoipUserHotlineStatusHotlineState_Type=DisplayString
_AdGenVoipUserHotlineStatusHotlineState_Object=MibTableColumn
adGenVoipUserHotlineStatusHotlineState=_AdGenVoipUserHotlineStatusHotlineState_Object((1,3,6,1,4,1,664,5,70,20,2,1,1,1,1,3),_AdGenVoipUserHotlineStatusHotlineState_Type())
adGenVoipUserHotlineStatusHotlineState.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipUserHotlineStatusHotlineState.setStatus(_A)
_AdGenVoipScalarStatus_ObjectIdentity=ObjectIdentity
adGenVoipScalarStatus=_AdGenVoipScalarStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,20,2,2))
_AdGenVoipScalarStatusMaxSupportedSipTrunks_Type=Integer32
_AdGenVoipScalarStatusMaxSupportedSipTrunks_Object=MibScalar
adGenVoipScalarStatusMaxSupportedSipTrunks=_AdGenVoipScalarStatusMaxSupportedSipTrunks_Object((1,3,6,1,4,1,664,5,70,20,2,2,1),_AdGenVoipScalarStatusMaxSupportedSipTrunks_Type())
adGenVoipScalarStatusMaxSupportedSipTrunks.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipScalarStatusMaxSupportedSipTrunks.setStatus(_A)
_AdGenVoipScalarStatusNumberOfSipTrunks_Type=Integer32
_AdGenVoipScalarStatusNumberOfSipTrunks_Object=MibScalar
adGenVoipScalarStatusNumberOfSipTrunks=_AdGenVoipScalarStatusNumberOfSipTrunks_Object((1,3,6,1,4,1,664,5,70,20,2,2,2),_AdGenVoipScalarStatusNumberOfSipTrunks_Type())
adGenVoipScalarStatusNumberOfSipTrunks.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenVoipScalarStatusNumberOfSipTrunks.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'AdGenVoipTrunkName':AdGenVoipTrunkName,'AdGenVoipCallServiceClassName':AdGenVoipCallServiceClassName,'AdGenVoipUserNumber':AdGenVoipUserNumber,'AdGenVoipDialingProfileName':AdGenVoipDialingProfileName,'AdGenVoipCodecProfileName':AdGenVoipCodecProfileName,'AdGenVoipMediaProfileName':AdGenVoipMediaProfileName,_w:AdGenVoipCodecProfileType,'AdGenVoipCallFeatureProfileName':AdGenVoipCallFeatureProfileName,'AdGenVoipCallReverseLookupIfIndex':AdGenVoipCallReverseLookupIfIndex,'adGenVoipProvisioning':adGenVoipProvisioning,'adGenVoipTrunkProv':adGenVoipTrunkProv,'adGenVoipTrunkProvTable':adGenVoipTrunkProvTable,'adGenVoipTrunkProvEntry':adGenVoipTrunkProvEntry,_W:adGenVoipTrunkEntryIndex,'adGenVoipTrunkTransfer':adGenVoipTrunkTransfer,'adGenVoipDialPlanProv':adGenVoipDialPlanProv,'adGenVoipDialPlanProvCurrentNumber':adGenVoipDialPlanProvCurrentNumber,'adGenVoipDialPlanProvLastCreateError':adGenVoipDialPlanProvLastCreateError,'adGenVoipDialPlanProvTable':adGenVoipDialPlanProvTable,'adGenVoipDialPlanProvEntry':adGenVoipDialPlanProvEntry,_X:adGenVoipDialPlanPatternEntryIndex,'adGenVoipDialPlanRowStatus':adGenVoipDialPlanRowStatus,'adGenVoipDialPlanLastErrorString':adGenVoipDialPlanLastErrorString,'adGenVoipDialPlanType':adGenVoipDialPlanType,'adGenVoipDialPlanEmergencyNumber':adGenVoipDialPlanEmergencyNumber,'adGenVoipDialPlanExternalLineCode':adGenVoipDialPlanExternalLineCode,'adGenVoipSPREPatternProv':adGenVoipSPREPatternProv,'adGenVoipSPREPatternProvCurrentNumber':adGenVoipSPREPatternProvCurrentNumber,'adGenVoipSPREPatternProvLastCreateError':adGenVoipSPREPatternProvLastCreateError,'adGenVoipSPREPatternProvTable':adGenVoipSPREPatternProvTable,'adGenVoipSPREPatternProvEntry':adGenVoipSPREPatternProvEntry,_l:adGenVoipSPREPatternEntryIndex,'adGenVoipSPREPatternRowStatus':adGenVoipSPREPatternRowStatus,'adGenVoipSPREPatternLastErrorString':adGenVoipSPREPatternLastErrorString,'adGenVoipSPREPatternTone':adGenVoipSPREPatternTone,'adGenVoipCallServiceClassProv':adGenVoipCallServiceClassProv,'adGenVoipCallServiceClassProvCurrentNumber':adGenVoipCallServiceClassProvCurrentNumber,'adGenVoipCallServiceClassProvLastCreateError':adGenVoipCallServiceClassProvLastCreateError,'adGenVoipCallServiceClassProvTable':adGenVoipCallServiceClassProvTable,'adGenVoipCallServiceClassProvEntry':adGenVoipCallServiceClassProvEntry,_m:adGenVoipCallServiceClassEntryIndex,'adGenVoipCallServiceClassRowStatus':adGenVoipCallServiceClassRowStatus,'adGenVoipCallServiceClassLastErrorString':adGenVoipCallServiceClassLastErrorString,'adGenVoipCallServiceClass900Number':adGenVoipCallServiceClass900Number,'adGenVoipCallServiceClassExtensions':adGenVoipCallServiceClassExtensions,'adGenVoipCallServiceClassInternational':adGenVoipCallServiceClassInternational,'adGenVoipCallServiceClassLocal':adGenVoipCallServiceClassLocal,'adGenVoipCallServiceClassNational':adGenVoipCallServiceClassNational,'adGenVoipCallServiceClassOperatorAssisted':adGenVoipCallServiceClassOperatorAssisted,'adGenVoipCallServiceClassSpecifyCarrier':adGenVoipCallServiceClassSpecifyCarrier,'adGenVoipCallServiceClassTollFree':adGenVoipCallServiceClassTollFree,'adGenVoipCallServiceClassUser1':adGenVoipCallServiceClassUser1,'adGenVoipCallServiceClassUser2':adGenVoipCallServiceClassUser2,'adGenVoipCallServiceClassUser3':adGenVoipCallServiceClassUser3,'adGenVoipCallServiceConference':adGenVoipCallServiceConference,'adGenVoipCallServiceDisableCallWaiting':adGenVoipCallServiceDisableCallWaiting,'adGenVoipUserProv':adGenVoipUserProv,'adGenVoipUserProvCurrentNumber':adGenVoipUserProvCurrentNumber,'adGenVoipUserProvLastCreateError':adGenVoipUserProvLastCreateError,'adGenVoipUserProvTable':adGenVoipUserProvTable,'adGenVoipUserProvEntry':adGenVoipUserProvEntry,_n:adGenVoipUserEntryIndex,'adGenVoipUserRowStatus':adGenVoipUserRowStatus,'adGenVoipUserLastErrorString':adGenVoipUserLastErrorString,'adGenVoipUserFxsPort':adGenVoipUserFxsPort,'adGenVoipUserCallClass':adGenVoipUserCallClass,'adGenVoipUserCallWaiting':adGenVoipUserCallWaiting,'adGenVoipUserDialingProfile':adGenVoipUserDialingProfile,'adGenVoipUserHotlineEnabled':adGenVoipUserHotlineEnabled,'adGenVoipUserHotlineNumber':adGenVoipUserHotlineNumber,'adGenVoipUserSipTrunkManualSelect':adGenVoipUserSipTrunkManualSelect,'adGenVoipUserWarmlineEnabled':adGenVoipUserWarmlineEnabled,'adGenVoipUserWarmlineNumber':adGenVoipUserWarmlineNumber,'adGenVoipUserWarmlineDelay':adGenVoipUserWarmlineDelay,'adGenVoipUserProvBulkInstance':adGenVoipUserProvBulkInstance,'adGenVoipScalarProv':adGenVoipScalarProv,'adGenVoipScalarFlashhookMode':adGenVoipScalarFlashhookMode,'adGenVoipScalarConferenceMode':adGenVoipScalarConferenceMode,'adGenVoipScalarConfLocalOriginatorFlashhook':adGenVoipScalarConfLocalOriginatorFlashhook,'adGenVoipScalarConfLocalOriginatorOnhook':adGenVoipScalarConfLocalOriginatorOnhook,'adGenVoipScalarConfLocalPartyDisconnect':adGenVoipScalarConfLocalPartyDisconnect,'adGenVoipScalarRtpUdpOffset':adGenVoipScalarRtpUdpOffset,'adGenVoipScalarSPREMode':adGenVoipScalarSPREMode,'adGenVoipScalarInterdigitTimer':adGenVoipScalarInterdigitTimer,'adGenVoipScalarAlertingTimer':adGenVoipScalarAlertingTimer,'adGenVoipScalarTransferOnHangup':adGenVoipScalarTransferOnHangup,'adGenVoipScalarFlashhookThreholdMin':adGenVoipScalarFlashhookThreholdMin,'adGenVoipScalarFlashhookThreholdMax':adGenVoipScalarFlashhookThreholdMax,'adGenVoipScalarEmergencyNumberInhibitOnHook':adGenVoipScalarEmergencyNumberInhibitOnHook,'adGenVoipScalarEmergencyNumberRingingTimemout':adGenVoipScalarEmergencyNumberRingingTimemout,'adGenVoipScalarDefaultSipTrunk':adGenVoipScalarDefaultSipTrunk,'adGenVoipScalarConnectedTimer':adGenVoipScalarConnectedTimer,'adGenVoipSPREMapScalarProv':adGenVoipSPREMapScalarProv,'adGenVoipScalarSPREMapDisableCallWaiting':adGenVoipScalarSPREMapDisableCallWaiting,'adGenVoipScalarSPREMapDNDDisableEnable':adGenVoipScalarSPREMapDNDDisableEnable,'adGenVoipScalarSPREMapBlockCallerID':adGenVoipScalarSPREMapBlockCallerID,'adGenVoipDialingProfileProv':adGenVoipDialingProfileProv,'adGenVoipDialingProfileDialPlanProv':adGenVoipDialingProfileDialPlanProv,'adGenVoipDialingProfileDialPlanProvCurrentNumber':adGenVoipDialingProfileDialPlanProvCurrentNumber,'adGenVoipDialingProfileDialPlanProvLastCreateError':adGenVoipDialingProfileDialPlanProvLastCreateError,'adGenVoipDialingProfileDialPlanProvTable':adGenVoipDialingProfileDialPlanProvTable,'adGenVoipDialingProfileDialPlanProvEntry':adGenVoipDialingProfileDialPlanProvEntry,_p:adGenVoipDialingProfileDialPlanPatternEntryIndex,'adGenVoipDialingProfileDialPlanRowStatus':adGenVoipDialingProfileDialPlanRowStatus,'adGenVoipDialingProfileDialPlanLastErrorString':adGenVoipDialingProfileDialPlanLastErrorString,'adGenVoipDialingProfileDialPlanType':adGenVoipDialingProfileDialPlanType,'adGenVoipDialingProfileDialPlanEmergencyNumber':adGenVoipDialingProfileDialPlanEmergencyNumber,'adGenVoipDialingProfileDialPlanExternalLineCode':adGenVoipDialingProfileDialPlanExternalLineCode,'adGenVoipDialingProfileDialPlanPattern':adGenVoipDialingProfileDialPlanPattern,'adGenVoipDialingProfileDialPlanDialingProfile':adGenVoipDialingProfileDialPlanDialingProfile,'adGenVoipDialingProfileSPREPatternProv':adGenVoipDialingProfileSPREPatternProv,'adGenVoipDialingProfileSPREPatternProvCurrentNumber':adGenVoipDialingProfileSPREPatternProvCurrentNumber,'adGenVoipDialingProfileSPREPatternProvLastCreateError':adGenVoipDialingProfileSPREPatternProvLastCreateError,'adGenVoipDialingProfileSPREPatternProvTable':adGenVoipDialingProfileSPREPatternProvTable,'adGenVoipDialingProfileSPREPatternProvEntry':adGenVoipDialingProfileSPREPatternProvEntry,_q:adGenVoipDialingProfileSPREPatternEntryIndex,'adGenVoipDialingProfileSPREPatternRowStatus':adGenVoipDialingProfileSPREPatternRowStatus,'adGenVoipDialingProfileSPREPatternLastErrorString':adGenVoipDialingProfileSPREPatternLastErrorString,'adGenVoipDialingProfileSPREPatternTone':adGenVoipDialingProfileSPREPatternTone,'adGenVoipDialingProfileSPREPattern':adGenVoipDialingProfileSPREPattern,'adGenVoipDialingProfileSPREPatternDialingProfile':adGenVoipDialingProfileSPREPatternDialingProfile,'adGenVoipDialingProfileExternalLineCodeProv':adGenVoipDialingProfileExternalLineCodeProv,'adGenVoipDialingProfileExternalLineCodeProvCurrentNumber':adGenVoipDialingProfileExternalLineCodeProvCurrentNumber,'adGenVoipDialingProfileExternalLineCodeProvLastCreateError':adGenVoipDialingProfileExternalLineCodeProvLastCreateError,'adGenVoipDialingProfileExternalLineCodeProvTable':adGenVoipDialingProfileExternalLineCodeProvTable,'adGenVoipDialingProfileExternalLineCodeProvEntry':adGenVoipDialingProfileExternalLineCodeProvEntry,_r:adGenVoipDialingProfileExternalLineCodeEntryIndex,'adGenVoipDialingProfileExternalLineCodeRowStatus':adGenVoipDialingProfileExternalLineCodeRowStatus,'adGenVoipDialingProfileExternalLineCodeLastErrorString':adGenVoipDialingProfileExternalLineCodeLastErrorString,'adGenVoipDialingProfileExternalLineCodeTone':adGenVoipDialingProfileExternalLineCodeTone,'adGenVoipDialingProfileExternalLineCodePattern':adGenVoipDialingProfileExternalLineCodePattern,'adGenVoipDialingProfileExternalLineCodeDialingProfile':adGenVoipDialingProfileExternalLineCodeDialingProfile,'adGenVoipDialingProfileProvExt':adGenVoipDialingProfileProvExt,'adGenVoipDialingProfileProvExtTable':adGenVoipDialingProfileProvExtTable,'adGenVoipDialingProfileProvExtEntry':adGenVoipDialingProfileProvExtEntry,_s:adGenVoipDialingProfileProvExtEntryIndex,'adGenVoipDialingProfileProvExtNumVoiceUsers':adGenVoipDialingProfileProvExtNumVoiceUsers,'adGenVoipDialingProfileProvExtRemoveProfile':adGenVoipDialingProfileProvExtRemoveProfile,'adGenVoipDialingProfileCommonProv':adGenVoipDialingProfileCommonProv,'adGenVoipDialingProfileCommonProvCurrentNumber':adGenVoipDialingProfileCommonProvCurrentNumber,'adGenVoipDialingProfileCommonProvLastCreateError':adGenVoipDialingProfileCommonProvLastCreateError,'adGenVoipDialingProfileCommonProvTable':adGenVoipDialingProfileCommonProvTable,'adGenVoipDialingProfileCommonProvEntry':adGenVoipDialingProfileCommonProvEntry,_u:adGenVoipDialingProfileCommonProvEntryIndex,'adGenVoipDialingProfileCommonProvNumVoiceUsers':adGenVoipDialingProfileCommonProvNumVoiceUsers,'adGenVoipDialingProfileCommonProvRemoveProfile':adGenVoipDialingProfileCommonProvRemoveProfile,'adGenVoipDialingProfileCommonProvDescription':adGenVoipDialingProfileCommonProvDescription,'adGenVoipDialingProfileCommonProvRowStatus':adGenVoipDialingProfileCommonProvRowStatus,'adGenVoipDialingProfileCommonProvLastErrorString':adGenVoipDialingProfileCommonProvLastErrorString,'adGenVoipCodecProfileNameProv':adGenVoipCodecProfileNameProv,'adGenVoipCodecProfileNameProvCurrentNumber':adGenVoipCodecProfileNameProvCurrentNumber,'adGenVoipCodecProfileNameProvLastCreateError':adGenVoipCodecProfileNameProvLastCreateError,'adGenVoipCodecProfileNameProvTable':adGenVoipCodecProfileNameProvTable,'adGenVoipCodecProfileNameProvEntry':adGenVoipCodecProfileNameProvEntry,_T:adGenVoipCodecProfileNameProvIndex,'adGenVoipCodecProfileNameProvRowStatus':adGenVoipCodecProfileNameProvRowStatus,'adGenVoipCodecProfileNameProvLastErrorString':adGenVoipCodecProfileNameProvLastErrorString,'adGenVoipCodecProfilePreferenceLastCreateError':adGenVoipCodecProfilePreferenceLastCreateError,'adGenVoipCodecProfileProv':adGenVoipCodecProfileProv,'adGenVoipCodecProfileProvTable':adGenVoipCodecProfileProvTable,'adGenVoipCodecProfileProvEntry':adGenVoipCodecProfileProvEntry,_v:adGenVoipCodecProfileProvIndex,'adGenVoipCodecProfileProvRowStatus':adGenVoipCodecProfileProvRowStatus,'adGenVoipCodecProfileProvLastErrorString':adGenVoipCodecProfileProvLastErrorString,'adGenVoipCodecProfileProvPreference':adGenVoipCodecProfileProvPreference,'adGenVoipMediaProfileProv':adGenVoipMediaProfileProv,'adGenVoipMediaProfileProvCurrentNumber':adGenVoipMediaProfileProvCurrentNumber,'adGenVoipMediaProfileProvLastCreateError':adGenVoipMediaProfileProvLastCreateError,'adGenVoipMediaProfileProvTable':adGenVoipMediaProfileProvTable,'adGenVoipMediaProfileProvEntry':adGenVoipMediaProfileProvEntry,_x:adGenVoipMediaProfileProvEntryIndex,'adGenVoipMediaProfileProvRowStatus':adGenVoipMediaProfileProvRowStatus,'adGenVoipMediaProfileProvLastErrorString':adGenVoipMediaProfileProvLastErrorString,'adGenVoipMediaProfileProvRtpFramePktization':adGenVoipMediaProfileProvRtpFramePktization,'adGenVoipMediaProfileProvRtpPktDelayNominal':adGenVoipMediaProfileProvRtpPktDelayNominal,'adGenVoipMediaProfileProvRtpPktDelayMaximum':adGenVoipMediaProfileProvRtpPktDelayMaximum,'adGenVoipMediaProfileProvRtpDtmfRelay':adGenVoipMediaProfileProvRtpDtmfRelay,'adGenVoipMediaProfileProvRtpQosDscp':adGenVoipMediaProfileProvRtpQosDscp,'adGenVoipMediaProfileProvRtpLocalPortMin':adGenVoipMediaProfileProvRtpLocalPortMin,'adGenVoipMediaProfileProvRtpLocalPortMax':adGenVoipMediaProfileProvRtpLocalPortMax,'adGenVoipMediaProfileProvFaxMode':adGenVoipMediaProfileProvFaxMode,'adGenVoipMediaProfileProvEchoCancellation':adGenVoipMediaProfileProvEchoCancellation,'adGenVoipMediaProfileProvFlashHookMin':adGenVoipMediaProfileProvFlashHookMin,'adGenVoipMediaProfileProvFlashHookMax':adGenVoipMediaProfileProvFlashHookMax,'adGenVoipMediaProfileProvVAD':adGenVoipMediaProfileProvVAD,'adGenVoipCallFeatureProfileProv':adGenVoipCallFeatureProfileProv,'adGenVoipCallFeatureProfileCurrentNumber':adGenVoipCallFeatureProfileCurrentNumber,'adGenVoipCallFeatureProfileLastCreateError':adGenVoipCallFeatureProfileLastCreateError,'adGenVoipCallFeatureProfileProvTable':adGenVoipCallFeatureProfileProvTable,'adGenVoipCallFeatureProfileProvEntry':adGenVoipCallFeatureProfileProvEntry,_y:adGenVoipCallFeatureProfileEntryIndex,'adGenVoipCallFeatureProfileRowStatus':adGenVoipCallFeatureProfileRowStatus,'adGenVoipCallFeatureProfileLastErrorString':adGenVoipCallFeatureProfileLastErrorString,'adGenVoipCallFeatureProfileEmergencyNumberRingingTimeout':adGenVoipCallFeatureProfileEmergencyNumberRingingTimeout,'adGenVoipCallFeatureProfileEmergencyNumberOnhook':adGenVoipCallFeatureProfileEmergencyNumberOnhook,'adGenVoipCallFeatureProfileCallWaiting':adGenVoipCallFeatureProfileCallWaiting,'adGenVoipCallFeatureProfileCallerIdInbound':adGenVoipCallFeatureProfileCallerIdInbound,'adGenVoipCallFeatureProfileCallerIdOutbound':adGenVoipCallFeatureProfileCallerIdOutbound,'adGenVoipCallFeatureProfileTransferOnHangup':adGenVoipCallFeatureProfileTransferOnHangup,'adGenVoipCallFeatureProfileTimeoutAlerting':adGenVoipCallFeatureProfileTimeoutAlerting,'adGenVoipCallFeatureProfileTimeoutInterdigit':adGenVoipCallFeatureProfileTimeoutInterdigit,'adGenVoipCallFeatureProfileConference':adGenVoipCallFeatureProfileConference,'adGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook':adGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook,'adGenVoipCallFeatureProfileFeatureMode':adGenVoipCallFeatureProfileFeatureMode,'adGenVoipUserReverseLookup':adGenVoipUserReverseLookup,'adGenVoipUserReverseLookupTable':adGenVoipUserReverseLookupTable,'adGenVoipUserReverseLookupTableEntry':adGenVoipUserReverseLookupTableEntry,_z:adGenVoipUserReverseLookupTableEntryIndex,'adGenVoipUserReverseLookupTableUserName':adGenVoipUserReverseLookupTableUserName,'adGenVoipSDPProv':adGenVoipSDPProv,'adGenVoipSDPGrammarPtime':adGenVoipSDPGrammarPtime,'adGenVoipSDPGrammarSuppressSilenceSupp':adGenVoipSDPGrammarSuppressSilenceSupp,'adGenVoipStatus':adGenVoipStatus,'adGenVoipUserStatus':adGenVoipUserStatus,'adGenVoipUserHotlineStatus':adGenVoipUserHotlineStatus,'adGenVoipUserHotlineStatusTable':adGenVoipUserHotlineStatusTable,'adGenVoipUserHotlineStatusTableEntry':adGenVoipUserHotlineStatusTableEntry,_A0:adGenVoipUserHotlineStatusEntryIndex,'adGenVoipUserHotlineStatusNumber':adGenVoipUserHotlineStatusNumber,'adGenVoipUserHotlineStatusHotlineState':adGenVoipUserHotlineStatusHotlineState,'adGenVoipScalarStatus':adGenVoipScalarStatus,'adGenVoipScalarStatusMaxSupportedSipTrunks':adGenVoipScalarStatusMaxSupportedSipTrunks,'adGenVoipScalarStatusNumberOfSipTrunks':adGenVoipScalarStatusNumberOfSipTrunks,'adGenVoipIdentity':adGenVoipIdentity})