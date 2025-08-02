_G='swPPPoECirIDInsertPortIndex'
_F='PPPOE-MGMT-MIB'
_E='disabled'
_D='enabled'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
swPPPoEMIB=ModuleIdentity((1,3,6,1,4,1,171,12,79))
_SwPPPoEMgmtCtrl_ObjectIdentity=ObjectIdentity
swPPPoEMgmtCtrl=_SwPPPoEMgmtCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,79,1))
class _SwPPPoECirIDInsertState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwPPPoECirIDInsertState_Type.__name__=_B
_SwPPPoECirIDInsertState_Object=MibScalar
swPPPoECirIDInsertState=_SwPPPoECirIDInsertState_Object((1,3,6,1,4,1,171,12,79,1,1),_SwPPPoECirIDInsertState_Type())
swPPPoECirIDInsertState.setMaxAccess(_C)
if mibBuilder.loadTexts:swPPPoECirIDInsertState.setStatus(_A)
_SwPPPoECirIDInsertPortMgmt_ObjectIdentity=ObjectIdentity
swPPPoECirIDInsertPortMgmt=_SwPPPoECirIDInsertPortMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,79,1,2))
_SwPPPoECirIDInsertPortTable_Object=MibTable
swPPPoECirIDInsertPortTable=_SwPPPoECirIDInsertPortTable_Object((1,3,6,1,4,1,171,12,79,1,2,1))
if mibBuilder.loadTexts:swPPPoECirIDInsertPortTable.setStatus(_A)
_SwPPPoECirIDInsertPortEntry_Object=MibTableRow
swPPPoECirIDInsertPortEntry=_SwPPPoECirIDInsertPortEntry_Object((1,3,6,1,4,1,171,12,79,1,2,1,1))
swPPPoECirIDInsertPortEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:swPPPoECirIDInsertPortEntry.setStatus(_A)
class _SwPPPoECirIDInsertPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwPPPoECirIDInsertPortIndex_Type.__name__=_B
_SwPPPoECirIDInsertPortIndex_Object=MibTableColumn
swPPPoECirIDInsertPortIndex=_SwPPPoECirIDInsertPortIndex_Object((1,3,6,1,4,1,171,12,79,1,2,1,1,1),_SwPPPoECirIDInsertPortIndex_Type())
swPPPoECirIDInsertPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:swPPPoECirIDInsertPortIndex.setStatus(_A)
class _SwPPPoECirIDInsertPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_SwPPPoECirIDInsertPortState_Type.__name__=_B
_SwPPPoECirIDInsertPortState_Object=MibTableColumn
swPPPoECirIDInsertPortState=_SwPPPoECirIDInsertPortState_Object((1,3,6,1,4,1,171,12,79,1,2,1,1,2),_SwPPPoECirIDInsertPortState_Type())
swPPPoECirIDInsertPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swPPPoECirIDInsertPortState.setStatus(_A)
class _SwPPPoECirIDInsertPortCirID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('switch-ip',1),('switch-mac',2),('udf-string',3)))
_SwPPPoECirIDInsertPortCirID_Type.__name__=_B
_SwPPPoECirIDInsertPortCirID_Object=MibTableColumn
swPPPoECirIDInsertPortCirID=_SwPPPoECirIDInsertPortCirID_Object((1,3,6,1,4,1,171,12,79,1,2,1,1,3),_SwPPPoECirIDInsertPortCirID_Type())
swPPPoECirIDInsertPortCirID.setMaxAccess(_C)
if mibBuilder.loadTexts:swPPPoECirIDInsertPortCirID.setStatus(_A)
_SwPPPoECirIDInsertPortUDFString_Type=DisplayString
_SwPPPoECirIDInsertPortUDFString_Object=MibTableColumn
swPPPoECirIDInsertPortUDFString=_SwPPPoECirIDInsertPortUDFString_Object((1,3,6,1,4,1,171,12,79,1,2,1,1,4),_SwPPPoECirIDInsertPortUDFString_Type())
swPPPoECirIDInsertPortUDFString.setMaxAccess(_C)
if mibBuilder.loadTexts:swPPPoECirIDInsertPortUDFString.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'swPPPoEMIB':swPPPoEMIB,'swPPPoEMgmtCtrl':swPPPoEMgmtCtrl,'swPPPoECirIDInsertState':swPPPoECirIDInsertState,'swPPPoECirIDInsertPortMgmt':swPPPoECirIDInsertPortMgmt,'swPPPoECirIDInsertPortTable':swPPPoECirIDInsertPortTable,'swPPPoECirIDInsertPortEntry':swPPPoECirIDInsertPortEntry,_G:swPPPoECirIDInsertPortIndex,'swPPPoECirIDInsertPortState':swPPPoECirIDInsertPortState,'swPPPoECirIDInsertPortCirID':swPPPoECirIDInsertPortCirID,'swPPPoECirIDInsertPortUDFString':swPPPoECirIDInsertPortUDFString})