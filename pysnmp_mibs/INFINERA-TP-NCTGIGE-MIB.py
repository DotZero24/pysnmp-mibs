_P='nctGigEGroup'
_O='interfaceTypeNCT'
_N='nctGigEPeerChassisType'
_M='nctGigEPeerMcmSlotNum'
_L='nctGigEPeerChassisId'
_K='nctGigEPeerChassisSerNum'
_J='nctGigEPeerPortId'
_I='nctGigEForwardingState'
_H='nctGigEPortType'
_G='InfnChassisType'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='INFINERA-TP-NCTGIGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnChassisType,InfnNctType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths',_G,'InfnNctType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nctGigEMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,12))
if mibBuilder.loadTexts:nctGigEMIB.setRevisions(('2008-10-20 00:00',))
_NctGigETable_Object=MibTable
nctGigETable=_NctGigETable_Object((1,3,6,1,4,1,21296,2,2,2,2,12,1))
if mibBuilder.loadTexts:nctGigETable.setStatus(_A)
_NctGigEEntry_Object=MibTableRow
nctGigEEntry=_NctGigEEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,12,1,1))
nctGigEEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nctGigEEntry.setStatus(_A)
class _NctGigEPortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('nct',2),('gige',3)))
_NctGigEPortType_Type.__name__=_D
_NctGigEPortType_Object=MibTableColumn
nctGigEPortType=_NctGigEPortType_Object((1,3,6,1,4,1,21296,2,2,2,2,12,1,1,1),_NctGigEPortType_Type())
nctGigEPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:nctGigEPortType.setStatus(_A)
class _NctGigEForwardingState_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('enabled',2),('unknown',3)))
_NctGigEForwardingState_Type.__name__=_D
_NctGigEForwardingState_Object=MibTableColumn
nctGigEForwardingState=_NctGigEForwardingState_Object((1,3,6,1,4,1,21296,2,2,2,2,12,1,1,2),_NctGigEForwardingState_Type())
nctGigEForwardingState.setMaxAccess(_C)
if mibBuilder.loadTexts:nctGigEForwardingState.setStatus(_A)
class _NctGigEPeerPortId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('nct1',2),('nct2',3),('gige',4)))
_NctGigEPeerPortId_Type.__name__=_D
_NctGigEPeerPortId_Object=MibTableColumn
nctGigEPeerPortId=_NctGigEPeerPortId_Object((1,3,6,1,4,1,21296,2,2,2,2,12,1,1,3),_NctGigEPeerPortId_Type())
nctGigEPeerPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:nctGigEPeerPortId.setStatus(_A)
_NctGigEPeerChassisSerNum_Type=DisplayString
_NctGigEPeerChassisSerNum_Object=MibTableColumn
nctGigEPeerChassisSerNum=_NctGigEPeerChassisSerNum_Object((1,3,6,1,4,1,21296,2,2,2,2,12,1,1,4),_NctGigEPeerChassisSerNum_Type())
nctGigEPeerChassisSerNum.setMaxAccess(_C)
if mibBuilder.loadTexts:nctGigEPeerChassisSerNum.setStatus(_A)
_NctGigEPeerChassisId_Type=DisplayString
_NctGigEPeerChassisId_Object=MibTableColumn
nctGigEPeerChassisId=_NctGigEPeerChassisId_Object((1,3,6,1,4,1,21296,2,2,2,2,12,1,1,5),_NctGigEPeerChassisId_Type())
nctGigEPeerChassisId.setMaxAccess(_C)
if mibBuilder.loadTexts:nctGigEPeerChassisId.setStatus(_A)
class _NctGigEPeerMcmSlotNum_Type(Integer32):defaultValue=0
_NctGigEPeerMcmSlotNum_Type.__name__=_D
_NctGigEPeerMcmSlotNum_Object=MibTableColumn
nctGigEPeerMcmSlotNum=_NctGigEPeerMcmSlotNum_Object((1,3,6,1,4,1,21296,2,2,2,2,12,1,1,6),_NctGigEPeerMcmSlotNum_Type())
nctGigEPeerMcmSlotNum.setMaxAccess(_C)
if mibBuilder.loadTexts:nctGigEPeerMcmSlotNum.setStatus(_A)
class _NctGigEPeerChassisType_Type(InfnChassisType):defaultValue=1
_NctGigEPeerChassisType_Type.__name__=_G
_NctGigEPeerChassisType_Object=MibTableColumn
nctGigEPeerChassisType=_NctGigEPeerChassisType_Object((1,3,6,1,4,1,21296,2,2,2,2,12,1,1,7),_NctGigEPeerChassisType_Type())
nctGigEPeerChassisType.setMaxAccess(_C)
if mibBuilder.loadTexts:nctGigEPeerChassisType.setStatus(_A)
_InterfaceTypeNCT_Type=InfnNctType
_InterfaceTypeNCT_Object=MibTableColumn
interfaceTypeNCT=_InterfaceTypeNCT_Object((1,3,6,1,4,1,21296,2,2,2,2,12,1,1,8),_InterfaceTypeNCT_Type())
interfaceTypeNCT.setMaxAccess('read-write')
if mibBuilder.loadTexts:interfaceTypeNCT.setStatus(_A)
_NctGigEConformance_ObjectIdentity=ObjectIdentity
nctGigEConformance=_NctGigEConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,12,3))
_NctGigECompliances_ObjectIdentity=ObjectIdentity
nctGigECompliances=_NctGigECompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,12,3,1))
_NctGigEGroups_ObjectIdentity=ObjectIdentity
nctGigEGroups=_NctGigEGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,12,3,2))
nctGigEGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,12,3,2,1))
nctGigEGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:nctGigEGroup.setStatus(_A)
nctGigECompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,12,3,1,1))
nctGigECompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:nctGigECompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nctGigEMIB':nctGigEMIB,'nctGigETable':nctGigETable,'nctGigEEntry':nctGigEEntry,_H:nctGigEPortType,_I:nctGigEForwardingState,_J:nctGigEPeerPortId,_K:nctGigEPeerChassisSerNum,_L:nctGigEPeerChassisId,_M:nctGigEPeerMcmSlotNum,_N:nctGigEPeerChassisType,_O:interfaceTypeNCT,'nctGigEConformance':nctGigEConformance,'nctGigECompliances':nctGigECompliances,'nctGigECompliance':nctGigECompliance,'nctGigEGroups':nctGigEGroups,_P:nctGigEGroup})