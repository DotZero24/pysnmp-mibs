_F='not-accessible'
_E='atIpAddressAddr'
_D='atIpAddressAddrType'
_C='AT-IP-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
atIpMib=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,602))
if mibBuilder.loadTexts:atIpMib.setRevisions(('2010-06-14 05:09','2008-11-10 00:00'))
class AtIpAddressAssignmentType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notSet',0),('primary',1),('secondary',2)))
_AtIpAddressTable_Object=MibTable
atIpAddressTable=_AtIpAddressTable_Object((1,3,6,1,4,1,207,8,4,4,4,602,1))
if mibBuilder.loadTexts:atIpAddressTable.setStatus(_A)
_AtIpAddressEntry_Object=MibTableRow
atIpAddressEntry=_AtIpAddressEntry_Object((1,3,6,1,4,1,207,8,4,4,4,602,1,1))
atIpAddressEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:atIpAddressEntry.setStatus(_A)
_AtIpAddressAddrType_Type=InetAddressType
_AtIpAddressAddrType_Object=MibTableColumn
atIpAddressAddrType=_AtIpAddressAddrType_Object((1,3,6,1,4,1,207,8,4,4,4,602,1,1,1),_AtIpAddressAddrType_Type())
atIpAddressAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:atIpAddressAddrType.setStatus(_A)
_AtIpAddressAddr_Type=InetAddress
_AtIpAddressAddr_Object=MibTableColumn
atIpAddressAddr=_AtIpAddressAddr_Object((1,3,6,1,4,1,207,8,4,4,4,602,1,1,2),_AtIpAddressAddr_Type())
atIpAddressAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:atIpAddressAddr.setStatus(_A)
_AtIpAddressPrefixLen_Type=Integer32
_AtIpAddressPrefixLen_Object=MibTableColumn
atIpAddressPrefixLen=_AtIpAddressPrefixLen_Object((1,3,6,1,4,1,207,8,4,4,4,602,1,1,3),_AtIpAddressPrefixLen_Type())
atIpAddressPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:atIpAddressPrefixLen.setStatus(_A)
_AtIpAddressLabel_Type=DisplayString
_AtIpAddressLabel_Object=MibTableColumn
atIpAddressLabel=_AtIpAddressLabel_Object((1,3,6,1,4,1,207,8,4,4,4,602,1,1,4),_AtIpAddressLabel_Type())
atIpAddressLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:atIpAddressLabel.setStatus(_A)
_AtIpAddressIfIndex_Type=InterfaceIndex
_AtIpAddressIfIndex_Object=MibTableColumn
atIpAddressIfIndex=_AtIpAddressIfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,602,1,1,5),_AtIpAddressIfIndex_Type())
atIpAddressIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atIpAddressIfIndex.setStatus(_A)
_AtIpAddressAssignmentType_Type=AtIpAddressAssignmentType
_AtIpAddressAssignmentType_Object=MibTableColumn
atIpAddressAssignmentType=_AtIpAddressAssignmentType_Object((1,3,6,1,4,1,207,8,4,4,4,602,1,1,6),_AtIpAddressAssignmentType_Type())
atIpAddressAssignmentType.setMaxAccess(_B)
if mibBuilder.loadTexts:atIpAddressAssignmentType.setStatus(_A)
_AtIpAddressRowStatus_Type=RowStatus
_AtIpAddressRowStatus_Object=MibTableColumn
atIpAddressRowStatus=_AtIpAddressRowStatus_Object((1,3,6,1,4,1,207,8,4,4,4,602,1,1,7),_AtIpAddressRowStatus_Type())
atIpAddressRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atIpAddressRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'AtIpAddressAssignmentType':AtIpAddressAssignmentType,'atIpMib':atIpMib,'atIpAddressTable':atIpAddressTable,'atIpAddressEntry':atIpAddressEntry,_D:atIpAddressAddrType,_E:atIpAddressAddr,'atIpAddressPrefixLen':atIpAddressPrefixLen,'atIpAddressLabel':atIpAddressLabel,'atIpAddressIfIndex':atIpAddressIfIndex,'atIpAddressAssignmentType':atIpAddressAssignmentType,'atIpAddressRowStatus':atIpAddressRowStatus})