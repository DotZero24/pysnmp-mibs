_H='read-write'
_G='enable'
_F='disable'
_E='raisecomNMSACPAddrIndex'
_D='RAISECOM-NMS-ACC-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
raisecomNMSAccessControl=ModuleIdentity((1,3,6,1,4,1,8886,1,5))
_RaisecomNMSACPAddressTable_Object=MibTable
raisecomNMSACPAddressTable=_RaisecomNMSACPAddressTable_Object((1,3,6,1,4,1,8886,1,5,1))
if mibBuilder.loadTexts:raisecomNMSACPAddressTable.setStatus(_A)
_RaisecomNMSACPAddressEntry_Object=MibTableRow
raisecomNMSACPAddressEntry=_RaisecomNMSACPAddressEntry_Object((1,3,6,1,4,1,8886,1,5,1,1))
raisecomNMSACPAddressEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:raisecomNMSACPAddressEntry.setStatus(_A)
class _RaisecomNMSACPAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_RaisecomNMSACPAddrIndex_Type.__name__=_B
_RaisecomNMSACPAddrIndex_Object=MibTableColumn
raisecomNMSACPAddrIndex=_RaisecomNMSACPAddrIndex_Object((1,3,6,1,4,1,8886,1,5,1,1,1),_RaisecomNMSACPAddrIndex_Type())
raisecomNMSACPAddrIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:raisecomNMSACPAddrIndex.setStatus(_A)
_RaisecomNMSACPAddrIPAddress_Type=IpAddress
_RaisecomNMSACPAddrIPAddress_Object=MibTableColumn
raisecomNMSACPAddrIPAddress=_RaisecomNMSACPAddrIPAddress_Object((1,3,6,1,4,1,8886,1,5,1,1,2),_RaisecomNMSACPAddrIPAddress_Type())
raisecomNMSACPAddrIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomNMSACPAddrIPAddress.setStatus(_A)
_RaisecomNMSACPAddrNetMask_Type=IpAddress
_RaisecomNMSACPAddrNetMask_Object=MibTableColumn
raisecomNMSACPAddrNetMask=_RaisecomNMSACPAddrNetMask_Object((1,3,6,1,4,1,8886,1,5,1,1,3),_RaisecomNMSACPAddrNetMask_Type())
raisecomNMSACPAddrNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomNMSACPAddrNetMask.setStatus(_A)
_RaisecomNMSACPAddrRowStatus_Type=RowStatus
_RaisecomNMSACPAddrRowStatus_Object=MibTableColumn
raisecomNMSACPAddrRowStatus=_RaisecomNMSACPAddrRowStatus_Object((1,3,6,1,4,1,8886,1,5,1,1,4),_RaisecomNMSACPAddrRowStatus_Type())
raisecomNMSACPAddrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomNMSACPAddrRowStatus.setStatus(_A)
class _RaisecomTelnetAccessControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_RaisecomTelnetAccessControlStatus_Type.__name__=_B
_RaisecomTelnetAccessControlStatus_Object=MibScalar
raisecomTelnetAccessControlStatus=_RaisecomTelnetAccessControlStatus_Object((1,3,6,1,4,1,8886,1,5,2),_RaisecomTelnetAccessControlStatus_Type())
raisecomTelnetAccessControlStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:raisecomTelnetAccessControlStatus.setStatus(_A)
class _RaisecomWebAccessControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_RaisecomWebAccessControlStatus_Type.__name__=_B
_RaisecomWebAccessControlStatus_Object=MibScalar
raisecomWebAccessControlStatus=_RaisecomWebAccessControlStatus_Object((1,3,6,1,4,1,8886,1,5,3),_RaisecomWebAccessControlStatus_Type())
raisecomWebAccessControlStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:raisecomWebAccessControlStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'raisecomNMSAccessControl':raisecomNMSAccessControl,'raisecomNMSACPAddressTable':raisecomNMSACPAddressTable,'raisecomNMSACPAddressEntry':raisecomNMSACPAddressEntry,_E:raisecomNMSACPAddrIndex,'raisecomNMSACPAddrIPAddress':raisecomNMSACPAddrIPAddress,'raisecomNMSACPAddrNetMask':raisecomNMSACPAddrNetMask,'raisecomNMSACPAddrRowStatus':raisecomNMSACPAddrRowStatus,'raisecomTelnetAccessControlStatus':raisecomTelnetAccessControlStatus,'raisecomWebAccessControlStatus':raisecomWebAccessControlStatus})