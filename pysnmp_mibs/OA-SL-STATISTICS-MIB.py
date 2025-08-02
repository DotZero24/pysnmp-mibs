_I='oaSlStatMandatoryGroup'
_H='oaSlStatAggrOctets'
_G='oaSlStatGenSupport'
_F='oaSlStatServiceLevel'
_E='oaSlStatPortIndex'
_D='read-only'
_C='Integer32'
_B='OA-SL-STATISTICS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oaSlStatistics=ModuleIdentity((1,3,6,1,4,1,629,1,50,10,9))
if mibBuilder.loadTexts:oaSlStatistics.setRevisions(('2007-03-18 00:00',))
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_NbSwitchG1_ObjectIdentity=ObjectIdentity
nbSwitchG1=_NbSwitchG1_ObjectIdentity((1,3,6,1,4,1,629,1))
_NbSwitchG1Il_ObjectIdentity=ObjectIdentity
nbSwitchG1Il=_NbSwitchG1Il_ObjectIdentity((1,3,6,1,4,1,629,1,50))
_NbPortParams_ObjectIdentity=ObjectIdentity
nbPortParams=_NbPortParams_ObjectIdentity((1,3,6,1,4,1,629,1,50,10))
class _OaSlStatGenSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
_OaSlStatGenSupport_Type.__name__=_C
_OaSlStatGenSupport_Object=MibScalar
oaSlStatGenSupport=_OaSlStatGenSupport_Object((1,3,6,1,4,1,629,1,50,10,9,1),_OaSlStatGenSupport_Type())
oaSlStatGenSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:oaSlStatGenSupport.setStatus(_A)
_OaSlStatTable_Object=MibTable
oaSlStatTable=_OaSlStatTable_Object((1,3,6,1,4,1,629,1,50,10,9,2))
if mibBuilder.loadTexts:oaSlStatTable.setStatus(_A)
_OaSlStatEntry_Object=MibTableRow
oaSlStatEntry=_OaSlStatEntry_Object((1,3,6,1,4,1,629,1,50,10,9,2,1))
oaSlStatEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:oaSlStatEntry.setStatus(_A)
class _OaSlStatPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_OaSlStatPortIndex_Type.__name__=_C
_OaSlStatPortIndex_Object=MibTableColumn
oaSlStatPortIndex=_OaSlStatPortIndex_Object((1,3,6,1,4,1,629,1,50,10,9,2,1,1),_OaSlStatPortIndex_Type())
oaSlStatPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:oaSlStatPortIndex.setStatus(_A)
class _OaSlStatServiceLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_OaSlStatServiceLevel_Type.__name__=_C
_OaSlStatServiceLevel_Object=MibTableColumn
oaSlStatServiceLevel=_OaSlStatServiceLevel_Object((1,3,6,1,4,1,629,1,50,10,9,2,1,2),_OaSlStatServiceLevel_Type())
oaSlStatServiceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:oaSlStatServiceLevel.setStatus(_A)
_OaSlStatAggrOctets_Type=Counter64
_OaSlStatAggrOctets_Object=MibTableColumn
oaSlStatAggrOctets=_OaSlStatAggrOctets_Object((1,3,6,1,4,1,629,1,50,10,9,2,1,3),_OaSlStatAggrOctets_Type())
oaSlStatAggrOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:oaSlStatAggrOctets.setStatus(_A)
_OaSlStatConformance_ObjectIdentity=ObjectIdentity
oaSlStatConformance=_OaSlStatConformance_ObjectIdentity((1,3,6,1,4,1,629,1,50,10,9,101))
_OaSlStatMIBCompliances_ObjectIdentity=ObjectIdentity
oaSlStatMIBCompliances=_OaSlStatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,629,1,50,10,9,101,1))
_OaSlStatMIBGroups_ObjectIdentity=ObjectIdentity
oaSlStatMIBGroups=_OaSlStatMIBGroups_ObjectIdentity((1,3,6,1,4,1,629,1,50,10,9,101,2))
oaSlStatMandatoryGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,10,9,101,2,1))
oaSlStatMandatoryGroup.setObjects(*((_B,_G),(_B,_E),(_B,_F),(_B,_H)))
if mibBuilder.loadTexts:oaSlStatMandatoryGroup.setStatus(_A)
oaSlStatMIBCompliance=ModuleCompliance((1,3,6,1,4,1,629,1,50,10,9,101,1,1))
oaSlStatMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:oaSlStatMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nbase':nbase,'nbSwitchG1':nbSwitchG1,'nbSwitchG1Il':nbSwitchG1Il,'nbPortParams':nbPortParams,'oaSlStatistics':oaSlStatistics,_G:oaSlStatGenSupport,'oaSlStatTable':oaSlStatTable,'oaSlStatEntry':oaSlStatEntry,_E:oaSlStatPortIndex,_F:oaSlStatServiceLevel,_H:oaSlStatAggrOctets,'oaSlStatConformance':oaSlStatConformance,'oaSlStatMIBCompliances':oaSlStatMIBCompliances,'oaSlStatMIBCompliance':oaSlStatMIBCompliance,'oaSlStatMIBGroups':oaSlStatMIBGroups,_I:oaSlStatMandatoryGroup})