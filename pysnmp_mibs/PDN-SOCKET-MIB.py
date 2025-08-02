_F='devSocketNumber'
_E='PDN-SOCKET-MIB'
_D='entPhysicalIndex'
_C='ENTITY-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_C,_D)
pdn_socket,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-socket')
SocketFamily,SocketState,SocketType=mibBuilder.importSymbols('PDN-TC','SocketFamily','SocketState','SocketType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TAddress','TextualConvention')
_DevSocketStatsMIBObjects_ObjectIdentity=ObjectIdentity
devSocketStatsMIBObjects=_DevSocketStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,19,1))
_DevSocketStatsTable_Object=MibTable
devSocketStatsTable=_DevSocketStatsTable_Object((1,3,6,1,4,1,1795,2,24,2,19,1,1))
if mibBuilder.loadTexts:devSocketStatsTable.setStatus(_A)
_DevSocketStatsEntry_Object=MibTableRow
devSocketStatsEntry=_DevSocketStatsEntry_Object((1,3,6,1,4,1,1795,2,24,2,19,1,1,1))
devSocketStatsEntry.setIndexNames((0,_C,_D),(0,_E,_F))
if mibBuilder.loadTexts:devSocketStatsEntry.setStatus(_A)
_DevSocketNumber_Type=Integer32
_DevSocketNumber_Object=MibTableColumn
devSocketNumber=_DevSocketNumber_Object((1,3,6,1,4,1,1795,2,24,2,19,1,1,1,1),_DevSocketNumber_Type())
devSocketNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:devSocketNumber.setStatus(_A)
_DevSocketName_Type=DisplayString
_DevSocketName_Object=MibTableColumn
devSocketName=_DevSocketName_Object((1,3,6,1,4,1,1795,2,24,2,19,1,1,1,2),_DevSocketName_Type())
devSocketName.setMaxAccess(_B)
if mibBuilder.loadTexts:devSocketName.setStatus(_A)
_DevSocketFamily_Type=SocketFamily
_DevSocketFamily_Object=MibTableColumn
devSocketFamily=_DevSocketFamily_Object((1,3,6,1,4,1,1795,2,24,2,19,1,1,1,3),_DevSocketFamily_Type())
devSocketFamily.setMaxAccess(_B)
if mibBuilder.loadTexts:devSocketFamily.setStatus(_A)
_DevSocketType_Type=SocketType
_DevSocketType_Object=MibTableColumn
devSocketType=_DevSocketType_Object((1,3,6,1,4,1,1795,2,24,2,19,1,1,1,4),_DevSocketType_Type())
devSocketType.setMaxAccess(_B)
if mibBuilder.loadTexts:devSocketType.setStatus(_A)
_DevSocketLocalAddress_Type=TAddress
_DevSocketLocalAddress_Object=MibTableColumn
devSocketLocalAddress=_DevSocketLocalAddress_Object((1,3,6,1,4,1,1795,2,24,2,19,1,1,1,5),_DevSocketLocalAddress_Type())
devSocketLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:devSocketLocalAddress.setStatus(_A)
_DevSocketRemoteAddress_Type=TAddress
_DevSocketRemoteAddress_Object=MibTableColumn
devSocketRemoteAddress=_DevSocketRemoteAddress_Object((1,3,6,1,4,1,1795,2,24,2,19,1,1,1,6),_DevSocketRemoteAddress_Type())
devSocketRemoteAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:devSocketRemoteAddress.setStatus(_A)
_DevSocketState_Type=SocketState
_DevSocketState_Object=MibTableColumn
devSocketState=_DevSocketState_Object((1,3,6,1,4,1,1795,2,24,2,19,1,1,1,7),_DevSocketState_Type())
devSocketState.setMaxAccess(_B)
if mibBuilder.loadTexts:devSocketState.setStatus(_A)
_DevSocketInputBytes_Type=Integer32
_DevSocketInputBytes_Object=MibTableColumn
devSocketInputBytes=_DevSocketInputBytes_Object((1,3,6,1,4,1,1795,2,24,2,19,1,1,1,8),_DevSocketInputBytes_Type())
devSocketInputBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:devSocketInputBytes.setStatus(_A)
_DevSocketOutputBytes_Type=Integer32
_DevSocketOutputBytes_Object=MibTableColumn
devSocketOutputBytes=_DevSocketOutputBytes_Object((1,3,6,1,4,1,1795,2,24,2,19,1,1,1,9),_DevSocketOutputBytes_Type())
devSocketOutputBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:devSocketOutputBytes.setStatus(_A)
_DevSocketPDUDrops_Type=Integer32
_DevSocketPDUDrops_Object=MibTableColumn
devSocketPDUDrops=_DevSocketPDUDrops_Object((1,3,6,1,4,1,1795,2,24,2,19,1,1,1,10),_DevSocketPDUDrops_Type())
devSocketPDUDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:devSocketPDUDrops.setStatus(_A)
_DevSocketByteDrops_Type=Integer32
_DevSocketByteDrops_Object=MibTableColumn
devSocketByteDrops=_DevSocketByteDrops_Object((1,3,6,1,4,1,1795,2,24,2,19,1,1,1,11),_DevSocketByteDrops_Type())
devSocketByteDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:devSocketByteDrops.setStatus(_A)
_DevSocketStatsMIBTraps_ObjectIdentity=ObjectIdentity
devSocketStatsMIBTraps=_DevSocketStatsMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,19,2))
mibBuilder.exportSymbols(_E,**{'devSocketStatsMIBObjects':devSocketStatsMIBObjects,'devSocketStatsTable':devSocketStatsTable,'devSocketStatsEntry':devSocketStatsEntry,_F:devSocketNumber,'devSocketName':devSocketName,'devSocketFamily':devSocketFamily,'devSocketType':devSocketType,'devSocketLocalAddress':devSocketLocalAddress,'devSocketRemoteAddress':devSocketRemoteAddress,'devSocketState':devSocketState,'devSocketInputBytes':devSocketInputBytes,'devSocketOutputBytes':devSocketOutputBytes,'devSocketPDUDrops':devSocketPDUDrops,'devSocketByteDrops':devSocketByteDrops,'devSocketStatsMIBTraps':devSocketStatsMIBTraps})