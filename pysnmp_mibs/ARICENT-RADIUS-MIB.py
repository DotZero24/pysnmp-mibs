_E='radiusExtServerIndex'
_D='ARICENT-RADIUS-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
futureRADIUSMIB=ModuleIdentity((1,3,6,1,4,1,2076,25))
if mibBuilder.loadTexts:futureRADIUSMIB.setRevisions(('2012-09-05 00:00',))
_RadiusExtClient_ObjectIdentity=ObjectIdentity
radiusExtClient=_RadiusExtClient_ObjectIdentity((1,3,6,1,4,1,2076,25,1))
_RadiusExtDebugMask_Type=Integer32
_RadiusExtDebugMask_Object=MibScalar
radiusExtDebugMask=_RadiusExtDebugMask_Object((1,3,6,1,4,1,2076,25,1,1),_RadiusExtDebugMask_Type())
radiusExtDebugMask.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusExtDebugMask.setStatus(_A)
class _RadiusMaxNoOfUserEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RadiusMaxNoOfUserEntries_Type.__name__=_C
_RadiusMaxNoOfUserEntries_Object=MibScalar
radiusMaxNoOfUserEntries=_RadiusMaxNoOfUserEntries_Object((1,3,6,1,4,1,2076,25,1,2),_RadiusMaxNoOfUserEntries_Type())
radiusMaxNoOfUserEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusMaxNoOfUserEntries.setStatus(_A)
_RadiusExtServerTable_Object=MibTable
radiusExtServerTable=_RadiusExtServerTable_Object((1,3,6,1,4,1,2076,25,1,3))
if mibBuilder.loadTexts:radiusExtServerTable.setStatus(_A)
_RadiusExtServerEntry_Object=MibTableRow
radiusExtServerEntry=_RadiusExtServerEntry_Object((1,3,6,1,4,1,2076,25,1,3,1))
radiusExtServerEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:radiusExtServerEntry.setStatus(_A)
_RadiusExtServerIndex_Type=InterfaceIndex
_RadiusExtServerIndex_Object=MibTableColumn
radiusExtServerIndex=_RadiusExtServerIndex_Object((1,3,6,1,4,1,2076,25,1,3,1,1),_RadiusExtServerIndex_Type())
radiusExtServerIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:radiusExtServerIndex.setStatus(_A)
_RadiusExtServerAddress_Type=IpAddress
_RadiusExtServerAddress_Object=MibTableColumn
radiusExtServerAddress=_RadiusExtServerAddress_Object((1,3,6,1,4,1,2076,25,1,3,1,2),_RadiusExtServerAddress_Type())
radiusExtServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusExtServerAddress.setStatus(_A)
class _RadiusExtServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auth',1),('acct',2),('both',3)))
_RadiusExtServerType_Type.__name__=_C
_RadiusExtServerType_Object=MibTableColumn
radiusExtServerType=_RadiusExtServerType_Object((1,3,6,1,4,1,2076,25,1,3,1,3),_RadiusExtServerType_Type())
radiusExtServerType.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusExtServerType.setStatus(_A)
_RadiusExtServerSharedSecret_Type=DisplayString
_RadiusExtServerSharedSecret_Object=MibTableColumn
radiusExtServerSharedSecret=_RadiusExtServerSharedSecret_Object((1,3,6,1,4,1,2076,25,1,3,1,4),_RadiusExtServerSharedSecret_Type())
radiusExtServerSharedSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusExtServerSharedSecret.setStatus(_A)
class _RadiusExtServerEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),('destroy',3)))
_RadiusExtServerEnabled_Type.__name__=_C
_RadiusExtServerEnabled_Object=MibTableColumn
radiusExtServerEnabled=_RadiusExtServerEnabled_Object((1,3,6,1,4,1,2076,25,1,3,1,5),_RadiusExtServerEnabled_Type())
radiusExtServerEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusExtServerEnabled.setStatus(_A)
class _RadiusExtServerResponseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_RadiusExtServerResponseTime_Type.__name__=_C
_RadiusExtServerResponseTime_Object=MibTableColumn
radiusExtServerResponseTime=_RadiusExtServerResponseTime_Object((1,3,6,1,4,1,2076,25,1,3,1,6),_RadiusExtServerResponseTime_Type())
radiusExtServerResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusExtServerResponseTime.setStatus(_A)
class _RadiusExtServerMaximumRetransmission_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_RadiusExtServerMaximumRetransmission_Type.__name__=_C
_RadiusExtServerMaximumRetransmission_Object=MibTableColumn
radiusExtServerMaximumRetransmission=_RadiusExtServerMaximumRetransmission_Object((1,3,6,1,4,1,2076,25,1,3,1,7),_RadiusExtServerMaximumRetransmission_Type())
radiusExtServerMaximumRetransmission.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusExtServerMaximumRetransmission.setStatus(_A)
_RadiusExtServerEntryStatus_Type=RowStatus
_RadiusExtServerEntryStatus_Object=MibTableColumn
radiusExtServerEntryStatus=_RadiusExtServerEntryStatus_Object((1,3,6,1,4,1,2076,25,1,3,1,8),_RadiusExtServerEntryStatus_Type())
radiusExtServerEntryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusExtServerEntryStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'futureRADIUSMIB':futureRADIUSMIB,'radiusExtClient':radiusExtClient,'radiusExtDebugMask':radiusExtDebugMask,'radiusMaxNoOfUserEntries':radiusMaxNoOfUserEntries,'radiusExtServerTable':radiusExtServerTable,'radiusExtServerEntry':radiusExtServerEntry,_E:radiusExtServerIndex,'radiusExtServerAddress':radiusExtServerAddress,'radiusExtServerType':radiusExtServerType,'radiusExtServerSharedSecret':radiusExtServerSharedSecret,'radiusExtServerEnabled':radiusExtServerEnabled,'radiusExtServerResponseTime':radiusExtServerResponseTime,'radiusExtServerMaximumRetransmission':radiusExtServerMaximumRetransmission,'radiusExtServerEntryStatus':radiusExtServerEntryStatus})