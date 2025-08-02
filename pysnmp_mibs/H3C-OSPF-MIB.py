_G='h3cOspfNetworkIpAddr'
_F='h3cOspfAreaId'
_E='h3cOspfProcessId'
_D='Integer32'
_C='not-accessible'
_B='H3C-OSPF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cOspf=ModuleIdentity((1,3,6,1,4,1,2011,10,2,161))
if mibBuilder.loadTexts:h3cOspf.setRevisions(('2014-12-17 17:00',))
_H3cOspfNetworkTable_Object=MibTable
h3cOspfNetworkTable=_H3cOspfNetworkTable_Object((1,3,6,1,4,1,2011,10,2,161,1))
if mibBuilder.loadTexts:h3cOspfNetworkTable.setStatus(_A)
_H3cOspfNetworkEntry_Object=MibTableRow
h3cOspfNetworkEntry=_H3cOspfNetworkEntry_Object((1,3,6,1,4,1,2011,10,2,161,1,1))
h3cOspfNetworkEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:h3cOspfNetworkEntry.setStatus(_A)
class _H3cOspfProcessId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cOspfProcessId_Type.__name__=_D
_H3cOspfProcessId_Object=MibTableColumn
h3cOspfProcessId=_H3cOspfProcessId_Object((1,3,6,1,4,1,2011,10,2,161,1,1,1),_H3cOspfProcessId_Type())
h3cOspfProcessId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOspfProcessId.setStatus(_A)
_H3cOspfAreaId_Type=IpAddress
_H3cOspfAreaId_Object=MibTableColumn
h3cOspfAreaId=_H3cOspfAreaId_Object((1,3,6,1,4,1,2011,10,2,161,1,1,2),_H3cOspfAreaId_Type())
h3cOspfAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOspfAreaId.setStatus(_A)
_H3cOspfNetworkIpAddr_Type=IpAddress
_H3cOspfNetworkIpAddr_Object=MibTableColumn
h3cOspfNetworkIpAddr=_H3cOspfNetworkIpAddr_Object((1,3,6,1,4,1,2011,10,2,161,1,1,3),_H3cOspfNetworkIpAddr_Type())
h3cOspfNetworkIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cOspfNetworkIpAddr.setStatus(_A)
_H3cOspfNetworkIpMask_Type=IpAddress
_H3cOspfNetworkIpMask_Object=MibTableColumn
h3cOspfNetworkIpMask=_H3cOspfNetworkIpMask_Object((1,3,6,1,4,1,2011,10,2,161,1,1,4),_H3cOspfNetworkIpMask_Type())
h3cOspfNetworkIpMask.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cOspfNetworkIpMask.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cOspf':h3cOspf,'h3cOspfNetworkTable':h3cOspfNetworkTable,'h3cOspfNetworkEntry':h3cOspfNetworkEntry,_E:h3cOspfProcessId,_F:h3cOspfAreaId,_G:h3cOspfNetworkIpAddr,'h3cOspfNetworkIpMask':h3cOspfNetworkIpMask})