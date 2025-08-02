_U='tmnxIPsecStaticSAGroup'
_T='tmnxIPsecStaticSADescription'
_S='tmnxIPsecStaticSASpi'
_R='tmnxIPsecStaticSAAuthKey'
_Q='tmnxIPsecStaticSAAuthAlgorithm'
_P='tmnxIPsecStaticSAProtocol'
_O='tmnxIPsecStaticSADirection'
_N='tmnxIPsecStaticSALastChanged'
_M='tmnxIPsecStaticSARowStatus'
_L='tmnxIPsecStaticSATableLastChange'
_K='TmnxAuthAlgorithm'
_J='TmnxIPsecProtocol'
_I='TmnxIPsecDirection2'
_H='tmnxIPsecStaticSAName'
_G='read-only'
_F='TNamedItemOrEmpty'
_E='Unsigned32'
_D='OctetString'
_C='read-create'
_B='TIMETRA-IPSEC-STATIC-SA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
timetraSRMIBModules,tmnxSRConfs,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRObjs')
TNamedItem,TNamedItemOrEmpty=mibBuilder.importSymbols('TIMETRA-TC-MIB','TNamedItem',_F)
timetraIPsecStaticSAMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,73))
if mibBuilder.loadTexts:timetraIPsecStaticSAMIBModule.setRevisions(('2009-12-14 00:00',))
class TmnxAuthAlgorithm(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('null',1),('md5',2),('sha1',3)))
class TmnxIPsecDirection2(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inbound',1),('outbound',2),('bidirectional',3)))
class TmnxIPsecProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ah',1),('esp',2)))
_TmnxIPsecStaticSAConformance_ObjectIdentity=ObjectIdentity
tmnxIPsecStaticSAConformance=_TmnxIPsecStaticSAConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,73))
_TmnxIPsecStaticSACompliances_ObjectIdentity=ObjectIdentity
tmnxIPsecStaticSACompliances=_TmnxIPsecStaticSACompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,73,1))
_TmnxIPsecStaticSAGroups_ObjectIdentity=ObjectIdentity
tmnxIPsecStaticSAGroups=_TmnxIPsecStaticSAGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,73,2))
_TmnxIPsecStaticSAObjects_ObjectIdentity=ObjectIdentity
tmnxIPsecStaticSAObjects=_TmnxIPsecStaticSAObjects_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,73))
_TmnxIPsecStaticSATableLastChange_Type=TimeStamp
_TmnxIPsecStaticSATableLastChange_Object=MibScalar
tmnxIPsecStaticSATableLastChange=_TmnxIPsecStaticSATableLastChange_Object((1,3,6,1,4,1,6527,3,1,2,73,1),_TmnxIPsecStaticSATableLastChange_Type())
tmnxIPsecStaticSATableLastChange.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxIPsecStaticSATableLastChange.setStatus(_A)
_TmnxIPsecStaticSATable_Object=MibTable
tmnxIPsecStaticSATable=_TmnxIPsecStaticSATable_Object((1,3,6,1,4,1,6527,3,1,2,73,2))
if mibBuilder.loadTexts:tmnxIPsecStaticSATable.setStatus(_A)
_TmnxIPsecStaticSAEntry_Object=MibTableRow
tmnxIPsecStaticSAEntry=_TmnxIPsecStaticSAEntry_Object((1,3,6,1,4,1,6527,3,1,2,73,2,1))
tmnxIPsecStaticSAEntry.setIndexNames((1,_B,_H))
if mibBuilder.loadTexts:tmnxIPsecStaticSAEntry.setStatus(_A)
_TmnxIPsecStaticSAName_Type=TNamedItem
_TmnxIPsecStaticSAName_Object=MibTableColumn
tmnxIPsecStaticSAName=_TmnxIPsecStaticSAName_Object((1,3,6,1,4,1,6527,3,1,2,73,2,1,1),_TmnxIPsecStaticSAName_Type())
tmnxIPsecStaticSAName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tmnxIPsecStaticSAName.setStatus(_A)
_TmnxIPsecStaticSARowStatus_Type=RowStatus
_TmnxIPsecStaticSARowStatus_Object=MibTableColumn
tmnxIPsecStaticSARowStatus=_TmnxIPsecStaticSARowStatus_Object((1,3,6,1,4,1,6527,3,1,2,73,2,1,2),_TmnxIPsecStaticSARowStatus_Type())
tmnxIPsecStaticSARowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIPsecStaticSARowStatus.setStatus(_A)
_TmnxIPsecStaticSALastChanged_Type=TimeStamp
_TmnxIPsecStaticSALastChanged_Object=MibTableColumn
tmnxIPsecStaticSALastChanged=_TmnxIPsecStaticSALastChanged_Object((1,3,6,1,4,1,6527,3,1,2,73,2,1,3),_TmnxIPsecStaticSALastChanged_Type())
tmnxIPsecStaticSALastChanged.setMaxAccess(_G)
if mibBuilder.loadTexts:tmnxIPsecStaticSALastChanged.setStatus(_A)
class _TmnxIPsecStaticSADirection_Type(TmnxIPsecDirection2):defaultValue=3
_TmnxIPsecStaticSADirection_Type.__name__=_I
_TmnxIPsecStaticSADirection_Object=MibTableColumn
tmnxIPsecStaticSADirection=_TmnxIPsecStaticSADirection_Object((1,3,6,1,4,1,6527,3,1,2,73,2,1,4),_TmnxIPsecStaticSADirection_Type())
tmnxIPsecStaticSADirection.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIPsecStaticSADirection.setStatus(_A)
class _TmnxIPsecStaticSAProtocol_Type(TmnxIPsecProtocol):defaultValue=2
_TmnxIPsecStaticSAProtocol_Type.__name__=_J
_TmnxIPsecStaticSAProtocol_Object=MibTableColumn
tmnxIPsecStaticSAProtocol=_TmnxIPsecStaticSAProtocol_Object((1,3,6,1,4,1,6527,3,1,2,73,2,1,5),_TmnxIPsecStaticSAProtocol_Type())
tmnxIPsecStaticSAProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIPsecStaticSAProtocol.setStatus(_A)
class _TmnxIPsecStaticSAAuthAlgorithm_Type(TmnxAuthAlgorithm):defaultValue=3
_TmnxIPsecStaticSAAuthAlgorithm_Type.__name__=_K
_TmnxIPsecStaticSAAuthAlgorithm_Object=MibTableColumn
tmnxIPsecStaticSAAuthAlgorithm=_TmnxIPsecStaticSAAuthAlgorithm_Object((1,3,6,1,4,1,6527,3,1,2,73,2,1,6),_TmnxIPsecStaticSAAuthAlgorithm_Type())
tmnxIPsecStaticSAAuthAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIPsecStaticSAAuthAlgorithm.setStatus(_A)
class _TmnxIPsecStaticSAAuthKey_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_TmnxIPsecStaticSAAuthKey_Type.__name__=_D
_TmnxIPsecStaticSAAuthKey_Object=MibTableColumn
tmnxIPsecStaticSAAuthKey=_TmnxIPsecStaticSAAuthKey_Object((1,3,6,1,4,1,6527,3,1,2,73,2,1,7),_TmnxIPsecStaticSAAuthKey_Type())
tmnxIPsecStaticSAAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIPsecStaticSAAuthKey.setStatus(_A)
class _TmnxIPsecStaticSASpi_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(256,16383))
_TmnxIPsecStaticSASpi_Type.__name__=_E
_TmnxIPsecStaticSASpi_Object=MibTableColumn
tmnxIPsecStaticSASpi=_TmnxIPsecStaticSASpi_Object((1,3,6,1,4,1,6527,3,1,2,73,2,1,8),_TmnxIPsecStaticSASpi_Type())
tmnxIPsecStaticSASpi.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIPsecStaticSASpi.setStatus(_A)
class _TmnxIPsecStaticSADescription_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_TmnxIPsecStaticSADescription_Type.__name__=_F
_TmnxIPsecStaticSADescription_Object=MibTableColumn
tmnxIPsecStaticSADescription=_TmnxIPsecStaticSADescription_Object((1,3,6,1,4,1,6527,3,1,2,73,2,1,9),_TmnxIPsecStaticSADescription_Type())
tmnxIPsecStaticSADescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxIPsecStaticSADescription.setStatus(_A)
tmnxIPsecStaticSAGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,73,2,1))
tmnxIPsecStaticSAGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:tmnxIPsecStaticSAGroup.setStatus(_A)
tmnxIPsecStaticSAV8v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,73,1,1))
tmnxIPsecStaticSAV8v0Compliance.setObjects((_B,_U))
if mibBuilder.loadTexts:tmnxIPsecStaticSAV8v0Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_K:TmnxAuthAlgorithm,_I:TmnxIPsecDirection2,_J:TmnxIPsecProtocol,'timetraIPsecStaticSAMIBModule':timetraIPsecStaticSAMIBModule,'tmnxIPsecStaticSAConformance':tmnxIPsecStaticSAConformance,'tmnxIPsecStaticSACompliances':tmnxIPsecStaticSACompliances,'tmnxIPsecStaticSAV8v0Compliance':tmnxIPsecStaticSAV8v0Compliance,'tmnxIPsecStaticSAGroups':tmnxIPsecStaticSAGroups,_U:tmnxIPsecStaticSAGroup,'tmnxIPsecStaticSAObjects':tmnxIPsecStaticSAObjects,_L:tmnxIPsecStaticSATableLastChange,'tmnxIPsecStaticSATable':tmnxIPsecStaticSATable,'tmnxIPsecStaticSAEntry':tmnxIPsecStaticSAEntry,_H:tmnxIPsecStaticSAName,_M:tmnxIPsecStaticSARowStatus,_N:tmnxIPsecStaticSALastChanged,_O:tmnxIPsecStaticSADirection,_P:tmnxIPsecStaticSAProtocol,_Q:tmnxIPsecStaticSAAuthAlgorithm,_R:tmnxIPsecStaticSAAuthKey,_S:tmnxIPsecStaticSASpi,_T:tmnxIPsecStaticSADescription})