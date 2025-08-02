_T='hpevapaDescription'
_S='hpevapaThreshold_Value'
_R='hpevapaActual_Value'
_Q='hpevapaDetect_Level'
_P='hpevapaCounter_Name'
_O='hpevapaObject_Name'
_N='hpevapaObject_Type'
_M='hpevapaObject_ID'
_L='hpevapaArray_Name'
_K='hpevapaArray_ID'
_J='hpevapaSeverity'
_I='hpevapaTime_Detect'
_H='hpevapaCategory'
_G='hpevapaEvent_Code'
_F='hpevapaSequence_Number'
_E='hpevapaServer'
_D='NotificationType'
_C='mandatory'
_B='read-only'
_A='EVAPA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_D,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_D,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,232))
_Hpevapa_ObjectIdentity=ObjectIdentity
hpevapa=_Hpevapa_ObjectIdentity((1,3,6,1,4,1,232,175))
_Hpevent_ObjectIdentity=ObjectIdentity
hpevent=_Hpevent_ObjectIdentity((1,3,6,1,4,1,232,175,1))
_HpevapaTraps_ObjectIdentity=ObjectIdentity
hpevapaTraps=_HpevapaTraps_ObjectIdentity((1,3,6,1,4,1,232,175,1,1))
_HpevapaServer_Type=DisplayString
_HpevapaServer_Object=MibScalar
hpevapaServer=_HpevapaServer_Object((1,3,6,1,4,1,232,175,1,1,1),_HpevapaServer_Type())
hpevapaServer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaServer.setStatus(_C)
_HpevapaSequence_Number_Type=OctetString
_HpevapaSequence_Number_Object=MibScalar
hpevapaSequence_Number=_HpevapaSequence_Number_Object((1,3,6,1,4,1,232,175,1,1,2),_HpevapaSequence_Number_Type())
hpevapaSequence_Number.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaSequence_Number.setStatus(_C)
_HpevapaEvent_Code_Type=Integer32
_HpevapaEvent_Code_Object=MibScalar
hpevapaEvent_Code=_HpevapaEvent_Code_Object((1,3,6,1,4,1,232,175,1,1,3),_HpevapaEvent_Code_Type())
hpevapaEvent_Code.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaEvent_Code.setStatus(_C)
_HpevapaCategory_Type=OctetString
_HpevapaCategory_Object=MibScalar
hpevapaCategory=_HpevapaCategory_Object((1,3,6,1,4,1,232,175,1,1,4),_HpevapaCategory_Type())
hpevapaCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaCategory.setStatus(_C)
_HpevapaTime_Detect_Type=DisplayString
_HpevapaTime_Detect_Object=MibScalar
hpevapaTime_Detect=_HpevapaTime_Detect_Object((1,3,6,1,4,1,232,175,1,1,5),_HpevapaTime_Detect_Type())
hpevapaTime_Detect.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaTime_Detect.setStatus(_C)
_HpevapaSeverity_Type=DisplayString
_HpevapaSeverity_Object=MibScalar
hpevapaSeverity=_HpevapaSeverity_Object((1,3,6,1,4,1,232,175,1,1,6),_HpevapaSeverity_Type())
hpevapaSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaSeverity.setStatus(_C)
_HpevapaArray_ID_Type=OctetString
_HpevapaArray_ID_Object=MibScalar
hpevapaArray_ID=_HpevapaArray_ID_Object((1,3,6,1,4,1,232,175,1,1,7),_HpevapaArray_ID_Type())
hpevapaArray_ID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaArray_ID.setStatus(_C)
_HpevapaArray_Name_Type=OctetString
_HpevapaArray_Name_Object=MibScalar
hpevapaArray_Name=_HpevapaArray_Name_Object((1,3,6,1,4,1,232,175,1,1,8),_HpevapaArray_Name_Type())
hpevapaArray_Name.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaArray_Name.setStatus(_C)
_HpevapaObject_ID_Type=OctetString
_HpevapaObject_ID_Object=MibScalar
hpevapaObject_ID=_HpevapaObject_ID_Object((1,3,6,1,4,1,232,175,1,1,9),_HpevapaObject_ID_Type())
hpevapaObject_ID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaObject_ID.setStatus(_C)
_HpevapaObject_Type_Type=OctetString
_HpevapaObject_Type_Object=MibScalar
hpevapaObject_Type=_HpevapaObject_Type_Object((1,3,6,1,4,1,232,175,1,1,10),_HpevapaObject_Type_Type())
hpevapaObject_Type.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaObject_Type.setStatus(_C)
_HpevapaObject_Name_Type=OctetString
_HpevapaObject_Name_Object=MibScalar
hpevapaObject_Name=_HpevapaObject_Name_Object((1,3,6,1,4,1,232,175,1,1,11),_HpevapaObject_Name_Type())
hpevapaObject_Name.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaObject_Name.setStatus(_C)
_HpevapaCounter_Name_Type=OctetString
_HpevapaCounter_Name_Object=MibScalar
hpevapaCounter_Name=_HpevapaCounter_Name_Object((1,3,6,1,4,1,232,175,1,1,12),_HpevapaCounter_Name_Type())
hpevapaCounter_Name.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaCounter_Name.setStatus(_C)
_HpevapaDetect_Level_Type=OctetString
_HpevapaDetect_Level_Object=MibScalar
hpevapaDetect_Level=_HpevapaDetect_Level_Object((1,3,6,1,4,1,232,175,1,1,13),_HpevapaDetect_Level_Type())
hpevapaDetect_Level.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaDetect_Level.setStatus(_C)
_HpevapaActual_Value_Type=OctetString
_HpevapaActual_Value_Object=MibScalar
hpevapaActual_Value=_HpevapaActual_Value_Object((1,3,6,1,4,1,232,175,1,1,14),_HpevapaActual_Value_Type())
hpevapaActual_Value.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaActual_Value.setStatus(_C)
_HpevapaThreshold_Value_Type=OctetString
_HpevapaThreshold_Value_Object=MibScalar
hpevapaThreshold_Value=_HpevapaThreshold_Value_Object((1,3,6,1,4,1,232,175,1,1,15),_HpevapaThreshold_Value_Type())
hpevapaThreshold_Value.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaThreshold_Value.setStatus(_C)
_HpevapaDescription_Type=OctetString
_HpevapaDescription_Object=MibScalar
hpevapaDescription=_HpevapaDescription_Object((1,3,6,1,4,1,232,175,1,1,16),_HpevapaDescription_Type())
hpevapaDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hpevapaDescription.setStatus(_C)
hpevapaAlarmsTrap=NotificationType((1,3,6,1,4,1,232,175,1,1,0,4))
hpevapaAlarmsTrap.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:hpevapaAlarmsTrap.setStatus('')
mibBuilder.exportSymbols(_A,**{'hp':hp,'hpevapa':hpevapa,'hpevent':hpevent,'hpevapaTraps':hpevapaTraps,'hpevapaAlarmsTrap':hpevapaAlarmsTrap,_E:hpevapaServer,_F:hpevapaSequence_Number,_G:hpevapaEvent_Code,_H:hpevapaCategory,_I:hpevapaTime_Detect,_J:hpevapaSeverity,_K:hpevapaArray_ID,_L:hpevapaArray_Name,_M:hpevapaObject_ID,_N:hpevapaObject_Type,_O:hpevapaObject_Name,_P:hpevapaCounter_Name,_Q:hpevapaDetect_Level,_R:hpevapaActual_Value,_S:hpevapaThreshold_Value,_T:hpevapaDescription})