_I='eltCfmMaIndex'
_H='eltCfmMdIndex'
_G='not-accessible'
_F='eltCfmMdName'
_E='OctetString'
_D='Unsigned32'
_C='read-create'
_B='ELTEX-MES-CFM-MIB'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesMng,=mibBuilder.importSymbols('ELTEX-MES','eltMesMng')
Dot1agCfmMpDirection,=mibBuilder.importSymbols('IEEE8021-CFM-MIB','Dot1agCfmMpDirection')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
VlanId,VlanIdOrNone=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId','VlanIdOrNone')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TAddress,TDomain,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TAddress','TDomain','TextualConvention','TimeInterval','TimeStamp','TruthValue')
eltMesCfmMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,23,1,774))
if mibBuilder.loadTexts:eltMesCfmMIB.setRevisions(('2013-03-19 00:00','2015-11-19 00:00'))
_EltMesCfmNotifications_ObjectIdentity=ObjectIdentity
eltMesCfmNotifications=_EltMesCfmNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,774,0))
_EltMesCfmMIBObjects_ObjectIdentity=ObjectIdentity
eltMesCfmMIBObjects=_EltMesCfmMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,774,1))
_EltMesCfmMd_ObjectIdentity=ObjectIdentity
eltMesCfmMd=_EltMesCfmMd_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,774,1,1))
_EltCfmMdTable_Object=MibTable
eltCfmMdTable=_EltCfmMdTable_Object((1,3,6,1,4,1,35265,1,23,1,774,1,1,1))
if mibBuilder.loadTexts:eltCfmMdTable.setStatus(_A)
_EltCfmMdEntry_Object=MibTableRow
eltCfmMdEntry=_EltCfmMdEntry_Object((1,3,6,1,4,1,35265,1,23,1,774,1,1,1,1))
eltCfmMdEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:eltCfmMdEntry.setStatus(_A)
class _EltCfmMdName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_EltCfmMdName_Type.__name__=_E
_EltCfmMdName_Object=MibTableColumn
eltCfmMdName=_EltCfmMdName_Object((1,3,6,1,4,1,35265,1,23,1,774,1,1,1,1,1),_EltCfmMdName_Type())
eltCfmMdName.setMaxAccess(_G)
if mibBuilder.loadTexts:eltCfmMdName.setStatus(_A)
class _EltCfmMdIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EltCfmMdIndex_Type.__name__=_D
_EltCfmMdIndex_Object=MibTableColumn
eltCfmMdIndex=_EltCfmMdIndex_Object((1,3,6,1,4,1,35265,1,23,1,774,1,1,1,1,2),_EltCfmMdIndex_Type())
eltCfmMdIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eltCfmMdIndex.setStatus(_A)
_EltCfmMdRowStatus_Type=RowStatus
_EltCfmMdRowStatus_Object=MibTableColumn
eltCfmMdRowStatus=_EltCfmMdRowStatus_Object((1,3,6,1,4,1,35265,1,23,1,774,1,1,1,1,3),_EltCfmMdRowStatus_Type())
eltCfmMdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:eltCfmMdRowStatus.setStatus(_A)
_EltMesCfmMa_ObjectIdentity=ObjectIdentity
eltMesCfmMa=_EltMesCfmMa_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,774,1,2))
_EltCfmMaTable_Object=MibTable
eltCfmMaTable=_EltCfmMaTable_Object((1,3,6,1,4,1,35265,1,23,1,774,1,2,1))
if mibBuilder.loadTexts:eltCfmMaTable.setStatus(_A)
_EltCfmMaEntry_Object=MibTableRow
eltCfmMaEntry=_EltCfmMaEntry_Object((1,3,6,1,4,1,35265,1,23,1,774,1,2,1,1))
eltCfmMaEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:eltCfmMaEntry.setStatus(_A)
class _EltCfmMaIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EltCfmMaIndex_Type.__name__=_D
_EltCfmMaIndex_Object=MibTableColumn
eltCfmMaIndex=_EltCfmMaIndex_Object((1,3,6,1,4,1,35265,1,23,1,774,1,2,1,1,1),_EltCfmMaIndex_Type())
eltCfmMaIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:eltCfmMaIndex.setStatus(_A)
_EltCfmMaDirection_Type=Dot1agCfmMpDirection
_EltCfmMaDirection_Object=MibTableColumn
eltCfmMaDirection=_EltCfmMaDirection_Object((1,3,6,1,4,1,35265,1,23,1,774,1,2,1,1,2),_EltCfmMaDirection_Type())
eltCfmMaDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:eltCfmMaDirection.setStatus(_A)
_EltCfmMaRowStatus_Type=RowStatus
_EltCfmMaRowStatus_Object=MibTableColumn
eltCfmMaRowStatus=_EltCfmMaRowStatus_Object((1,3,6,1,4,1,35265,1,23,1,774,1,2,1,1,3),_EltCfmMaRowStatus_Type())
eltCfmMaRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:eltCfmMaRowStatus.setStatus(_A)
_EltMesCfmConformance_ObjectIdentity=ObjectIdentity
eltMesCfmConformance=_EltMesCfmConformance_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,774,2))
mibBuilder.exportSymbols(_B,**{'eltMesCfmMIB':eltMesCfmMIB,'eltMesCfmNotifications':eltMesCfmNotifications,'eltMesCfmMIBObjects':eltMesCfmMIBObjects,'eltMesCfmMd':eltMesCfmMd,'eltCfmMdTable':eltCfmMdTable,'eltCfmMdEntry':eltCfmMdEntry,_F:eltCfmMdName,_H:eltCfmMdIndex,'eltCfmMdRowStatus':eltCfmMdRowStatus,'eltMesCfmMa':eltMesCfmMa,'eltCfmMaTable':eltCfmMaTable,'eltCfmMaEntry':eltCfmMaEntry,_I:eltCfmMaIndex,'eltCfmMaDirection':eltCfmMaDirection,'eltCfmMaRowStatus':eltCfmMaRowStatus,'eltMesCfmConformance':eltMesCfmConformance})