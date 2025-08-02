_F='hpnicfSlbgPortIndex'
_E='read-create'
_D='not-accessible'
_C='hpnicfSlbgGroupNumber'
_B='HPN-ICF-SLBG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfSlbg=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,130))
if mibBuilder.loadTexts:hpnicfSlbg.setRevisions(('2012-10-16 00:00',))
_HpnicfSlbgMibTable_ObjectIdentity=ObjectIdentity
hpnicfSlbgMibTable=_HpnicfSlbgMibTable_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,130,1))
_HpnicfSlbgGroupTable_Object=MibTable
hpnicfSlbgGroupTable=_HpnicfSlbgGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,130,1,1))
if mibBuilder.loadTexts:hpnicfSlbgGroupTable.setStatus(_A)
_HpnicfSlbgGroupEntry_Object=MibTableRow
hpnicfSlbgGroupEntry=_HpnicfSlbgGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,130,1,1,1))
hpnicfSlbgGroupEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:hpnicfSlbgGroupEntry.setStatus(_A)
_HpnicfSlbgGroupNumber_Type=Unsigned32
_HpnicfSlbgGroupNumber_Object=MibTableColumn
hpnicfSlbgGroupNumber=_HpnicfSlbgGroupNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,130,1,1,1,1),_HpnicfSlbgGroupNumber_Type())
hpnicfSlbgGroupNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSlbgGroupNumber.setStatus(_A)
class _HpnicfSlbgGroupSrvType_Type(Bits):namedValues=NamedValues(*(('ipv6',0),('ipv6mc',1),('tunnel',2),('multicastTunnel',3),('mpls',4)))
_HpnicfSlbgGroupSrvType_Type.__name__='Bits'
_HpnicfSlbgGroupSrvType_Object=MibTableColumn
hpnicfSlbgGroupSrvType=_HpnicfSlbgGroupSrvType_Object((1,3,6,1,4,1,11,2,14,11,15,2,130,1,1,1,2),_HpnicfSlbgGroupSrvType_Type())
hpnicfSlbgGroupSrvType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSlbgGroupSrvType.setStatus(_A)
_HpnicfSlbgGroupRowStatus_Type=RowStatus
_HpnicfSlbgGroupRowStatus_Object=MibTableColumn
hpnicfSlbgGroupRowStatus=_HpnicfSlbgGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,130,1,1,1,3),_HpnicfSlbgGroupRowStatus_Type())
hpnicfSlbgGroupRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSlbgGroupRowStatus.setStatus(_A)
_HpnicfSlbgPortTable_Object=MibTable
hpnicfSlbgPortTable=_HpnicfSlbgPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,130,1,2))
if mibBuilder.loadTexts:hpnicfSlbgPortTable.setStatus(_A)
_HpnicfSlbgPortEntry_Object=MibTableRow
hpnicfSlbgPortEntry=_HpnicfSlbgPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,130,1,2,1))
hpnicfSlbgPortEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:hpnicfSlbgPortEntry.setStatus(_A)
_HpnicfSlbgPortIndex_Type=InterfaceIndex
_HpnicfSlbgPortIndex_Object=MibTableColumn
hpnicfSlbgPortIndex=_HpnicfSlbgPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,130,1,2,1,1),_HpnicfSlbgPortIndex_Type())
hpnicfSlbgPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSlbgPortIndex.setStatus(_A)
_HpnicfSlbgPortAttachedGroupNumber_Type=Unsigned32
_HpnicfSlbgPortAttachedGroupNumber_Object=MibTableColumn
hpnicfSlbgPortAttachedGroupNumber=_HpnicfSlbgPortAttachedGroupNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,130,1,2,1,2),_HpnicfSlbgPortAttachedGroupNumber_Type())
hpnicfSlbgPortAttachedGroupNumber.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfSlbgPortAttachedGroupNumber.setStatus(_A)
_HpnicfSlbgPortSelectedGroupNumber_Type=Unsigned32
_HpnicfSlbgPortSelectedGroupNumber_Object=MibTableColumn
hpnicfSlbgPortSelectedGroupNumber=_HpnicfSlbgPortSelectedGroupNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,130,1,2,1,3),_HpnicfSlbgPortSelectedGroupNumber_Type())
hpnicfSlbgPortSelectedGroupNumber.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfSlbgPortSelectedGroupNumber.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfSlbg':hpnicfSlbg,'hpnicfSlbgMibTable':hpnicfSlbgMibTable,'hpnicfSlbgGroupTable':hpnicfSlbgGroupTable,'hpnicfSlbgGroupEntry':hpnicfSlbgGroupEntry,_C:hpnicfSlbgGroupNumber,'hpnicfSlbgGroupSrvType':hpnicfSlbgGroupSrvType,'hpnicfSlbgGroupRowStatus':hpnicfSlbgGroupRowStatus,'hpnicfSlbgPortTable':hpnicfSlbgPortTable,'hpnicfSlbgPortEntry':hpnicfSlbgPortEntry,_F:hpnicfSlbgPortIndex,'hpnicfSlbgPortAttachedGroupNumber':hpnicfSlbgPortAttachedGroupNumber,'hpnicfSlbgPortSelectedGroupNumber':hpnicfSlbgPortSelectedGroupNumber})