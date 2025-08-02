_d='cwTrapVarsTrapGroup5'
_c='cwTrapVarsTrapGroup4'
_b='cwTrapVarsTrapGroup3'
_a='cwTrapVarsTrapGroup2'
_Z='cwTrapVarsTrapGroup'
_Y='cwTrapThirdIndex'
_X='cwTrapSecondIndex'
_W='cwTrapReference'
_V='cwTrapAtmAddressType'
_U='cwTrapVarLength'
_T='OctetString'
_S='cwTrapSctMajorVersion'
_R='cwTrapSctId'
_Q='cwTrapSctType'
_P='cwTrapSctCardType'
_O='cwTrapCardRole'
_N='cwTrapPhysicalUnit'
_M='cwTrapPhysicalContainer'
_L='Unsigned32'
_K='cwTrapDisplayString'
_J='cwTrapOctetString'
_I='cwTrapLineModuleNumber'
_H='cwTrapPhysicalVendorType'
_G='cwTrapSlotNumber'
_F='cwTrapIndex'
_E='deprecated'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-WAN-TRAP-VARS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_T,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','TextualConvention')
ciscoWanTrapVarsMIB=ModuleIdentity((1,3,6,1,4,1,351,150,5))
if mibBuilder.loadTexts:ciscoWanTrapVarsMIB.setRevisions(('2002-11-26 00:00','2002-07-17 00:00','2001-11-07 00:00','2001-11-06 00:00','2001-07-26 00:00','1999-05-21 00:00'))
_CwTrapVarMIBObjects_ObjectIdentity=ObjectIdentity
cwTrapVarMIBObjects=_CwTrapVarMIBObjects_ObjectIdentity((1,3,6,1,4,1,351,150,5,1))
_CwTrapVars_ObjectIdentity=ObjectIdentity
cwTrapVars=_CwTrapVars_ObjectIdentity((1,3,6,1,4,1,351,150,5,1,1))
class _CwTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwTrapIndex_Type.__name__=_D
_CwTrapIndex_Object=MibScalar
cwTrapIndex=_CwTrapIndex_Object((1,3,6,1,4,1,351,150,5,1,1,1),_CwTrapIndex_Type())
cwTrapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapIndex.setStatus(_B)
class _CwTrapSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_CwTrapSlotNumber_Type.__name__=_D
_CwTrapSlotNumber_Object=MibScalar
cwTrapSlotNumber=_CwTrapSlotNumber_Object((1,3,6,1,4,1,351,150,5,1,1,2),_CwTrapSlotNumber_Type())
cwTrapSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapSlotNumber.setStatus(_B)
_CwTrapPhysicalVendorType_Type=AutonomousType
_CwTrapPhysicalVendorType_Object=MibScalar
cwTrapPhysicalVendorType=_CwTrapPhysicalVendorType_Object((1,3,6,1,4,1,351,150,5,1,1,3),_CwTrapPhysicalVendorType_Type())
cwTrapPhysicalVendorType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapPhysicalVendorType.setStatus(_B)
class _CwTrapLineModuleNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CwTrapLineModuleNumber_Type.__name__=_D
_CwTrapLineModuleNumber_Object=MibScalar
cwTrapLineModuleNumber=_CwTrapLineModuleNumber_Object((1,3,6,1,4,1,351,150,5,1,1,4),_CwTrapLineModuleNumber_Type())
cwTrapLineModuleNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapLineModuleNumber.setStatus(_B)
class _CwTrapOctetString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_CwTrapOctetString_Type.__name__=_T
_CwTrapOctetString_Object=MibScalar
cwTrapOctetString=_CwTrapOctetString_Object((1,3,6,1,4,1,351,150,5,1,1,5),_CwTrapOctetString_Type())
cwTrapOctetString.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapOctetString.setStatus(_B)
_CwTrapDisplayString_Type=DisplayString
_CwTrapDisplayString_Object=MibScalar
cwTrapDisplayString=_CwTrapDisplayString_Object((1,3,6,1,4,1,351,150,5,1,1,6),_CwTrapDisplayString_Type())
cwTrapDisplayString.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapDisplayString.setStatus(_B)
class _CwTrapPhysicalContainer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwTrapPhysicalContainer_Type.__name__=_D
_CwTrapPhysicalContainer_Object=MibScalar
cwTrapPhysicalContainer=_CwTrapPhysicalContainer_Object((1,3,6,1,4,1,351,150,5,1,1,7),_CwTrapPhysicalContainer_Type())
cwTrapPhysicalContainer.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapPhysicalContainer.setStatus(_B)
class _CwTrapPhysicalUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwTrapPhysicalUnit_Type.__name__=_D
_CwTrapPhysicalUnit_Object=MibScalar
cwTrapPhysicalUnit=_CwTrapPhysicalUnit_Object((1,3,6,1,4,1,351,150,5,1,1,8),_CwTrapPhysicalUnit_Type())
cwTrapPhysicalUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapPhysicalUnit.setStatus(_B)
class _CwTrapCardRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('t1',1),('e1',2),('t3',3),('e3',4)))
_CwTrapCardRole_Type.__name__=_D
_CwTrapCardRole_Object=MibScalar
cwTrapCardRole=_CwTrapCardRole_Object((1,3,6,1,4,1,351,150,5,1,1,9),_CwTrapCardRole_Type())
cwTrapCardRole.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapCardRole.setStatus(_B)
class _CwTrapSctCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('axsm',1),('axsme',2),('pxm1e',3),('hsfr',4)))
_CwTrapSctCardType_Type.__name__=_D
_CwTrapSctCardType_Object=MibScalar
cwTrapSctCardType=_CwTrapSctCardType_Object((1,3,6,1,4,1,351,150,5,1,1,10),_CwTrapSctCardType_Type())
cwTrapSctCardType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapSctCardType.setStatus(_B)
class _CwTrapSctType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('portSct',1),('cardSct',2)))
_CwTrapSctType_Type.__name__=_D
_CwTrapSctType_Object=MibScalar
cwTrapSctType=_CwTrapSctType_Object((1,3,6,1,4,1,351,150,5,1,1,11),_CwTrapSctType_Type())
cwTrapSctType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapSctType.setStatus(_B)
class _CwTrapSctId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CwTrapSctId_Type.__name__=_L
_CwTrapSctId_Object=MibScalar
cwTrapSctId=_CwTrapSctId_Object((1,3,6,1,4,1,351,150,5,1,1,12),_CwTrapSctId_Type())
cwTrapSctId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapSctId.setStatus(_B)
class _CwTrapSctMajorVersion_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CwTrapSctMajorVersion_Type.__name__=_L
_CwTrapSctMajorVersion_Object=MibScalar
cwTrapSctMajorVersion=_CwTrapSctMajorVersion_Object((1,3,6,1,4,1,351,150,5,1,1,13),_CwTrapSctMajorVersion_Type())
cwTrapSctMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapSctMajorVersion.setStatus(_B)
class _CwTrapVarLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CwTrapVarLength_Type.__name__=_L
_CwTrapVarLength_Object=MibScalar
cwTrapVarLength=_CwTrapVarLength_Object((1,3,6,1,4,1,351,150,5,1,1,14),_CwTrapVarLength_Type())
cwTrapVarLength.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapVarLength.setStatus(_B)
class _CwTrapAtmAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,8)));namedValues=NamedValues(*(('e164',3),('nsap',8)))
_CwTrapAtmAddressType_Type.__name__=_D
_CwTrapAtmAddressType_Object=MibScalar
cwTrapAtmAddressType=_CwTrapAtmAddressType_Object((1,3,6,1,4,1,351,150,5,1,1,15),_CwTrapAtmAddressType_Type())
cwTrapAtmAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapAtmAddressType.setStatus(_B)
class _CwTrapReference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CwTrapReference_Type.__name__=_D
_CwTrapReference_Object=MibScalar
cwTrapReference=_CwTrapReference_Object((1,3,6,1,4,1,351,150,5,1,1,16),_CwTrapReference_Type())
cwTrapReference.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapReference.setStatus(_B)
class _CwTrapSecondIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwTrapSecondIndex_Type.__name__=_D
_CwTrapSecondIndex_Object=MibScalar
cwTrapSecondIndex=_CwTrapSecondIndex_Object((1,3,6,1,4,1,351,150,5,1,1,17),_CwTrapSecondIndex_Type())
cwTrapSecondIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapSecondIndex.setStatus(_B)
class _CwTrapThirdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwTrapThirdIndex_Type.__name__=_D
_CwTrapThirdIndex_Object=MibScalar
cwTrapThirdIndex=_CwTrapThirdIndex_Object((1,3,6,1,4,1,351,150,5,1,1,18),_CwTrapThirdIndex_Type())
cwTrapThirdIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cwTrapThirdIndex.setStatus(_B)
_CwTrapVarsMIBConformance_ObjectIdentity=ObjectIdentity
cwTrapVarsMIBConformance=_CwTrapVarsMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,5,2))
_CwTrapVarsMIBCompliances_ObjectIdentity=ObjectIdentity
cwTrapVarsMIBCompliances=_CwTrapVarsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,5,2,1))
_CwTrapVarsMIBGroups_ObjectIdentity=ObjectIdentity
cwTrapVarsMIBGroups=_CwTrapVarsMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,5,2,2))
cwTrapVarsTrapGroup=ObjectGroup((1,3,6,1,4,1,351,150,5,2,2,1))
cwTrapVarsTrapGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:cwTrapVarsTrapGroup.setStatus(_E)
cwTrapVarsTrapGroup2=ObjectGroup((1,3,6,1,4,1,351,150,5,2,2,2))
cwTrapVarsTrapGroup2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:cwTrapVarsTrapGroup2.setStatus(_E)
cwTrapVarsTrapGroup3=ObjectGroup((1,3,6,1,4,1,351,150,5,2,2,3))
cwTrapVarsTrapGroup3.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:cwTrapVarsTrapGroup3.setStatus(_E)
cwTrapVarsTrapGroup4=ObjectGroup((1,3,6,1,4,1,351,150,5,2,2,4))
cwTrapVarsTrapGroup4.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:cwTrapVarsTrapGroup4.setStatus(_E)
cwTrapVarsTrapGroup5=ObjectGroup((1,3,6,1,4,1,351,150,5,2,2,5))
cwTrapVarsTrapGroup5.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:cwTrapVarsTrapGroup5.setStatus(_B)
cwTrapVarsCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,5,2,1,1))
cwTrapVarsCompliance.setObjects((_A,_Z))
if mibBuilder.loadTexts:cwTrapVarsCompliance.setStatus(_E)
cwTrapVarsCompliance2=ModuleCompliance((1,3,6,1,4,1,351,150,5,2,1,2))
cwTrapVarsCompliance2.setObjects((_A,_a))
if mibBuilder.loadTexts:cwTrapVarsCompliance2.setStatus(_E)
cwTrapVarsCompliance3=ModuleCompliance((1,3,6,1,4,1,351,150,5,2,1,3))
cwTrapVarsCompliance3.setObjects((_A,_b))
if mibBuilder.loadTexts:cwTrapVarsCompliance3.setStatus(_E)
cwTrapVarsCompliance4=ModuleCompliance((1,3,6,1,4,1,351,150,5,2,1,4))
cwTrapVarsCompliance4.setObjects((_A,_c))
if mibBuilder.loadTexts:cwTrapVarsCompliance4.setStatus(_E)
cwTrapVarsCompliance5=ModuleCompliance((1,3,6,1,4,1,351,150,5,2,1,5))
cwTrapVarsCompliance5.setObjects((_A,_d))
if mibBuilder.loadTexts:cwTrapVarsCompliance5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoWanTrapVarsMIB':ciscoWanTrapVarsMIB,'cwTrapVarMIBObjects':cwTrapVarMIBObjects,'cwTrapVars':cwTrapVars,_F:cwTrapIndex,_G:cwTrapSlotNumber,_H:cwTrapPhysicalVendorType,_I:cwTrapLineModuleNumber,_J:cwTrapOctetString,_K:cwTrapDisplayString,_M:cwTrapPhysicalContainer,_N:cwTrapPhysicalUnit,_O:cwTrapCardRole,_P:cwTrapSctCardType,_Q:cwTrapSctType,_R:cwTrapSctId,_S:cwTrapSctMajorVersion,_U:cwTrapVarLength,_V:cwTrapAtmAddressType,_W:cwTrapReference,_X:cwTrapSecondIndex,_Y:cwTrapThirdIndex,'cwTrapVarsMIBConformance':cwTrapVarsMIBConformance,'cwTrapVarsMIBCompliances':cwTrapVarsMIBCompliances,'cwTrapVarsCompliance':cwTrapVarsCompliance,'cwTrapVarsCompliance2':cwTrapVarsCompliance2,'cwTrapVarsCompliance3':cwTrapVarsCompliance3,'cwTrapVarsCompliance4':cwTrapVarsCompliance4,'cwTrapVarsCompliance5':cwTrapVarsCompliance5,'cwTrapVarsMIBGroups':cwTrapVarsMIBGroups,_Z:cwTrapVarsTrapGroup,_a:cwTrapVarsTrapGroup2,_b:cwTrapVarsTrapGroup3,_c:cwTrapVarsTrapGroup4,_d:cwTrapVarsTrapGroup5})