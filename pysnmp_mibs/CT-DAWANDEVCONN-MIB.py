_F='read-only'
_E='daWanConnectionIndex'
_D='daWanDeviceIndex'
_C='CT-DAWANDEVCONN-MIB'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cabletron,=mibBuilder.importSymbols('CTRON-OIDS','cabletron')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtSSA_ObjectIdentity=ObjectIdentity
ctSSA=_CtSSA_ObjectIdentity((1,3,6,1,4,1,52,4497))
_DaWanDevConn_ObjectIdentity=ObjectIdentity
daWanDevConn=_DaWanDevConn_ObjectIdentity((1,3,6,1,4,1,52,4497,23))
_DaWanDevConnTable_Object=MibTable
daWanDevConnTable=_DaWanDevConnTable_Object((1,3,6,1,4,1,52,4497,23,1))
if mibBuilder.loadTexts:daWanDevConnTable.setStatus(_A)
_DaWanDevConnEntry_Object=MibTableRow
daWanDevConnEntry=_DaWanDevConnEntry_Object((1,3,6,1,4,1,52,4497,23,1,1))
daWanDevConnEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:daWanDevConnEntry.setStatus(_A)
class _DaWanDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DaWanDeviceIndex_Type.__name__=_B
_DaWanDeviceIndex_Object=MibTableColumn
daWanDeviceIndex=_DaWanDeviceIndex_Object((1,3,6,1,4,1,52,4497,23,1,1,1),_DaWanDeviceIndex_Type())
daWanDeviceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:daWanDeviceIndex.setStatus(_A)
class _DaWanConnectionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DaWanConnectionIndex_Type.__name__=_B
_DaWanConnectionIndex_Object=MibTableColumn
daWanConnectionIndex=_DaWanConnectionIndex_Object((1,3,6,1,4,1,52,4497,23,1,1,2),_DaWanConnectionIndex_Type())
daWanConnectionIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:daWanConnectionIndex.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ctSSA':ctSSA,'daWanDevConn':daWanDevConn,'daWanDevConnTable':daWanDevConnTable,'daWanDevConnEntry':daWanDevConnEntry,_D:daWanDeviceIndex,_E:daWanConnectionIndex})