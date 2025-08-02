_F='h3cSlbgPortIndex'
_E='read-create'
_D='not-accessible'
_C='h3cSlbgGroupNumber'
_B='H3C-SLBG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cSlbg=ModuleIdentity((1,3,6,1,4,1,2011,10,2,130))
if mibBuilder.loadTexts:h3cSlbg.setRevisions(('2012-10-16 00:00',))
_H3cSlbgMibTable_ObjectIdentity=ObjectIdentity
h3cSlbgMibTable=_H3cSlbgMibTable_ObjectIdentity((1,3,6,1,4,1,2011,10,2,130,1))
_H3cSlbgGroupTable_Object=MibTable
h3cSlbgGroupTable=_H3cSlbgGroupTable_Object((1,3,6,1,4,1,2011,10,2,130,1,1))
if mibBuilder.loadTexts:h3cSlbgGroupTable.setStatus(_A)
_H3cSlbgGroupEntry_Object=MibTableRow
h3cSlbgGroupEntry=_H3cSlbgGroupEntry_Object((1,3,6,1,4,1,2011,10,2,130,1,1,1))
h3cSlbgGroupEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:h3cSlbgGroupEntry.setStatus(_A)
_H3cSlbgGroupNumber_Type=Unsigned32
_H3cSlbgGroupNumber_Object=MibTableColumn
h3cSlbgGroupNumber=_H3cSlbgGroupNumber_Object((1,3,6,1,4,1,2011,10,2,130,1,1,1,1),_H3cSlbgGroupNumber_Type())
h3cSlbgGroupNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSlbgGroupNumber.setStatus(_A)
class _H3cSlbgGroupSrvType_Type(Bits):namedValues=NamedValues(*(('ipv6',0),('ipv6mc',1),('tunnel',2),('multicastTunnel',3),('mpls',4)))
_H3cSlbgGroupSrvType_Type.__name__='Bits'
_H3cSlbgGroupSrvType_Object=MibTableColumn
h3cSlbgGroupSrvType=_H3cSlbgGroupSrvType_Object((1,3,6,1,4,1,2011,10,2,130,1,1,1,2),_H3cSlbgGroupSrvType_Type())
h3cSlbgGroupSrvType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSlbgGroupSrvType.setStatus(_A)
_H3cSlbgGroupRowStatus_Type=RowStatus
_H3cSlbgGroupRowStatus_Object=MibTableColumn
h3cSlbgGroupRowStatus=_H3cSlbgGroupRowStatus_Object((1,3,6,1,4,1,2011,10,2,130,1,1,1,3),_H3cSlbgGroupRowStatus_Type())
h3cSlbgGroupRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSlbgGroupRowStatus.setStatus(_A)
_H3cSlbgPortTable_Object=MibTable
h3cSlbgPortTable=_H3cSlbgPortTable_Object((1,3,6,1,4,1,2011,10,2,130,1,2))
if mibBuilder.loadTexts:h3cSlbgPortTable.setStatus(_A)
_H3cSlbgPortEntry_Object=MibTableRow
h3cSlbgPortEntry=_H3cSlbgPortEntry_Object((1,3,6,1,4,1,2011,10,2,130,1,2,1))
h3cSlbgPortEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:h3cSlbgPortEntry.setStatus(_A)
_H3cSlbgPortIndex_Type=InterfaceIndex
_H3cSlbgPortIndex_Object=MibTableColumn
h3cSlbgPortIndex=_H3cSlbgPortIndex_Object((1,3,6,1,4,1,2011,10,2,130,1,2,1,1),_H3cSlbgPortIndex_Type())
h3cSlbgPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSlbgPortIndex.setStatus(_A)
_H3cSlbgPortAttachedGroupNumber_Type=Unsigned32
_H3cSlbgPortAttachedGroupNumber_Object=MibTableColumn
h3cSlbgPortAttachedGroupNumber=_H3cSlbgPortAttachedGroupNumber_Object((1,3,6,1,4,1,2011,10,2,130,1,2,1,2),_H3cSlbgPortAttachedGroupNumber_Type())
h3cSlbgPortAttachedGroupNumber.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cSlbgPortAttachedGroupNumber.setStatus(_A)
_H3cSlbgPortSelectedGroupNumber_Type=Unsigned32
_H3cSlbgPortSelectedGroupNumber_Object=MibTableColumn
h3cSlbgPortSelectedGroupNumber=_H3cSlbgPortSelectedGroupNumber_Object((1,3,6,1,4,1,2011,10,2,130,1,2,1,3),_H3cSlbgPortSelectedGroupNumber_Type())
h3cSlbgPortSelectedGroupNumber.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cSlbgPortSelectedGroupNumber.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cSlbg':h3cSlbg,'h3cSlbgMibTable':h3cSlbgMibTable,'h3cSlbgGroupTable':h3cSlbgGroupTable,'h3cSlbgGroupEntry':h3cSlbgGroupEntry,_C:h3cSlbgGroupNumber,'h3cSlbgGroupSrvType':h3cSlbgGroupSrvType,'h3cSlbgGroupRowStatus':h3cSlbgGroupRowStatus,'h3cSlbgPortTable':h3cSlbgPortTable,'h3cSlbgPortEntry':h3cSlbgPortEntry,_F:h3cSlbgPortIndex,'h3cSlbgPortAttachedGroupNumber':h3cSlbgPortAttachedGroupNumber,'h3cSlbgPortSelectedGroupNumber':h3cSlbgPortSelectedGroupNumber})