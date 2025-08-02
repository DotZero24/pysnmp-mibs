_G='read-write'
_F='not-accessible'
_E='zyMacFilterVid'
_D='zyMacFilterMacAddress'
_C='Integer32'
_B='ZYXEL-MAC-FILTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelMacFilter=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,47))
_ZyxelMacFilterSetup_ObjectIdentity=ObjectIdentity
zyxelMacFilterSetup=_ZyxelMacFilterSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,47,1))
_ZyMacFilterMaxNumberOfRules_Type=Integer32
_ZyMacFilterMaxNumberOfRules_Object=MibScalar
zyMacFilterMaxNumberOfRules=_ZyMacFilterMaxNumberOfRules_Object((1,3,6,1,4,1,890,1,15,3,47,1,1),_ZyMacFilterMaxNumberOfRules_Type())
zyMacFilterMaxNumberOfRules.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyMacFilterMaxNumberOfRules.setStatus(_A)
_ZyxelMacFilterTable_Object=MibTable
zyxelMacFilterTable=_ZyxelMacFilterTable_Object((1,3,6,1,4,1,890,1,15,3,47,1,2))
if mibBuilder.loadTexts:zyxelMacFilterTable.setStatus(_A)
_ZyxelMacFilterEntry_Object=MibTableRow
zyxelMacFilterEntry=_ZyxelMacFilterEntry_Object((1,3,6,1,4,1,890,1,15,3,47,1,2,1))
zyxelMacFilterEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:zyxelMacFilterEntry.setStatus(_A)
_ZyMacFilterMacAddress_Type=MacAddress
_ZyMacFilterMacAddress_Object=MibTableColumn
zyMacFilterMacAddress=_ZyMacFilterMacAddress_Object((1,3,6,1,4,1,890,1,15,3,47,1,2,1,1),_ZyMacFilterMacAddress_Type())
zyMacFilterMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:zyMacFilterMacAddress.setStatus(_A)
_ZyMacFilterVid_Type=Integer32
_ZyMacFilterVid_Object=MibTableColumn
zyMacFilterVid=_ZyMacFilterVid_Object((1,3,6,1,4,1,890,1,15,3,47,1,2,1,2),_ZyMacFilterVid_Type())
zyMacFilterVid.setMaxAccess(_F)
if mibBuilder.loadTexts:zyMacFilterVid.setStatus(_A)
_ZyMacFilterName_Type=DisplayString
_ZyMacFilterName_Object=MibTableColumn
zyMacFilterName=_ZyMacFilterName_Object((1,3,6,1,4,1,890,1,15,3,47,1,2,1,3),_ZyMacFilterName_Type())
zyMacFilterName.setMaxAccess(_G)
if mibBuilder.loadTexts:zyMacFilterName.setStatus(_A)
class _ZyMacFilterAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('discardSource',1),('discardDestination',2),('both',3)))
_ZyMacFilterAction_Type.__name__=_C
_ZyMacFilterAction_Object=MibTableColumn
zyMacFilterAction=_ZyMacFilterAction_Object((1,3,6,1,4,1,890,1,15,3,47,1,2,1,4),_ZyMacFilterAction_Type())
zyMacFilterAction.setMaxAccess(_G)
if mibBuilder.loadTexts:zyMacFilterAction.setStatus(_A)
_ZyMacFilterRowStatus_Type=RowStatus
_ZyMacFilterRowStatus_Object=MibTableColumn
zyMacFilterRowStatus=_ZyMacFilterRowStatus_Object((1,3,6,1,4,1,890,1,15,3,47,1,2,1,5),_ZyMacFilterRowStatus_Type())
zyMacFilterRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyMacFilterRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelMacFilter':zyxelMacFilter,'zyxelMacFilterSetup':zyxelMacFilterSetup,'zyMacFilterMaxNumberOfRules':zyMacFilterMaxNumberOfRules,'zyxelMacFilterTable':zyxelMacFilterTable,'zyxelMacFilterEntry':zyxelMacFilterEntry,_D:zyMacFilterMacAddress,_E:zyMacFilterVid,'zyMacFilterName':zyMacFilterName,'zyMacFilterAction':zyMacFilterAction,'zyMacFilterRowStatus':zyMacFilterRowStatus})