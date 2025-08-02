_L='cVoaMIBBaseGroup'
_K='cVoaDesiredPower'
_J='cVoaAttenuationLastChange'
_I='cVoaAttenuation'
_H='cVoaAttenuationControlMode'
_G='cVoaDirection'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='CISCO-VOA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
OpticalIfDirection,=mibBuilder.importSymbols('CISCO-OPTICAL-MONITOR-MIB','OpticalIfDirection')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoVoaMIB=ModuleIdentity((1,3,6,1,4,1,9,9,262))
if mibBuilder.loadTexts:ciscoVoaMIB.setRevisions(('2002-05-07 00:00',))
class OpticalPowerInDbm(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,250),ValueRangeConstraint(-1000,-1000))
class OpticalAttenInDb(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,400))
_CVoaMIBObjects_ObjectIdentity=ObjectIdentity
cVoaMIBObjects=_CVoaMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,262,1))
_CVoaBaseGroup_ObjectIdentity=ObjectIdentity
cVoaBaseGroup=_CVoaBaseGroup_ObjectIdentity((1,3,6,1,4,1,9,9,262,1,1))
_CVoaTable_Object=MibTable
cVoaTable=_CVoaTable_Object((1,3,6,1,4,1,9,9,262,1,1,1))
if mibBuilder.loadTexts:cVoaTable.setStatus(_A)
_CVoaEntry_Object=MibTableRow
cVoaEntry=_CVoaEntry_Object((1,3,6,1,4,1,9,9,262,1,1,1,1))
cVoaEntry.setIndexNames((0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:cVoaEntry.setStatus(_A)
_CVoaDirection_Type=OpticalIfDirection
_CVoaDirection_Object=MibTableColumn
cVoaDirection=_CVoaDirection_Object((1,3,6,1,4,1,9,9,262,1,1,1,1,1),_CVoaDirection_Type())
cVoaDirection.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cVoaDirection.setStatus(_A)
class _CVoaAttenuationControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('automatic',2)))
_CVoaAttenuationControlMode_Type.__name__=_F
_CVoaAttenuationControlMode_Object=MibTableColumn
cVoaAttenuationControlMode=_CVoaAttenuationControlMode_Object((1,3,6,1,4,1,9,9,262,1,1,1,1,2),_CVoaAttenuationControlMode_Type())
cVoaAttenuationControlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cVoaAttenuationControlMode.setStatus(_A)
_CVoaAttenuation_Type=OpticalAttenInDb
_CVoaAttenuation_Object=MibTableColumn
cVoaAttenuation=_CVoaAttenuation_Object((1,3,6,1,4,1,9,9,262,1,1,1,1,3),_CVoaAttenuation_Type())
cVoaAttenuation.setMaxAccess(_C)
if mibBuilder.loadTexts:cVoaAttenuation.setStatus(_A)
_CVoaAttenuationLastChange_Type=TimeStamp
_CVoaAttenuationLastChange_Object=MibTableColumn
cVoaAttenuationLastChange=_CVoaAttenuationLastChange_Object((1,3,6,1,4,1,9,9,262,1,1,1,1,4),_CVoaAttenuationLastChange_Type())
cVoaAttenuationLastChange.setMaxAccess('read-only')
if mibBuilder.loadTexts:cVoaAttenuationLastChange.setStatus(_A)
_CVoaDesiredPower_Type=OpticalPowerInDbm
_CVoaDesiredPower_Object=MibTableColumn
cVoaDesiredPower=_CVoaDesiredPower_Object((1,3,6,1,4,1,9,9,262,1,1,1,1,5),_CVoaDesiredPower_Type())
cVoaDesiredPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cVoaDesiredPower.setStatus(_A)
_CVoaMIBConformance_ObjectIdentity=ObjectIdentity
cVoaMIBConformance=_CVoaMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,262,3))
_CVoaMIBCompliances_ObjectIdentity=ObjectIdentity
cVoaMIBCompliances=_CVoaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,262,3,1))
_CVoaMIBGroups_ObjectIdentity=ObjectIdentity
cVoaMIBGroups=_CVoaMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,262,3,2))
cVoaMIBBaseGroup=ObjectGroup((1,3,6,1,4,1,9,9,262,3,2,1))
cVoaMIBBaseGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cVoaMIBBaseGroup.setStatus(_A)
cVoaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,262,3,1,1))
cVoaMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:cVoaMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'OpticalPowerInDbm':OpticalPowerInDbm,'OpticalAttenInDb':OpticalAttenInDb,'ciscoVoaMIB':ciscoVoaMIB,'cVoaMIBObjects':cVoaMIBObjects,'cVoaBaseGroup':cVoaBaseGroup,'cVoaTable':cVoaTable,'cVoaEntry':cVoaEntry,_G:cVoaDirection,_H:cVoaAttenuationControlMode,_I:cVoaAttenuation,_J:cVoaAttenuationLastChange,_K:cVoaDesiredPower,'cVoaMIBConformance':cVoaMIBConformance,'cVoaMIBCompliances':cVoaMIBCompliances,'cVoaMIBCompliance':cVoaMIBCompliance,'cVoaMIBGroups':cVoaMIBGroups,_L:cVoaMIBBaseGroup})