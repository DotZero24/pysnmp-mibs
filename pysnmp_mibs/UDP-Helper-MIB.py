_I='swUDPHelperServerCtrlServer'
_H='swUDPHelperServerCtrlInterfaceName'
_G='read-create'
_F='swUDPHelperPortNumber'
_E='DisplayString'
_D='Integer32'
_C='not-accessible'
_B='UDP-Helper-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
swUDPHelperMIB=ModuleIdentity((1,3,6,1,4,1,171,12,99))
_SwUDPHelperMIBObjects_ObjectIdentity=ObjectIdentity
swUDPHelperMIBObjects=_SwUDPHelperMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,12,99,1))
_SwUDPHelperGeneralGroup_ObjectIdentity=ObjectIdentity
swUDPHelperGeneralGroup=_SwUDPHelperGeneralGroup_ObjectIdentity((1,3,6,1,4,1,171,12,99,1,1))
class _SwUDPHelperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SwUDPHelperState_Type.__name__=_D
_SwUDPHelperState_Object=MibScalar
swUDPHelperState=_SwUDPHelperState_Object((1,3,6,1,4,1,171,12,99,1,1,1),_SwUDPHelperState_Type())
swUDPHelperState.setMaxAccess('read-write')
if mibBuilder.loadTexts:swUDPHelperState.setStatus(_A)
_SwUDPHelperPortCtrlTable_Object=MibTable
swUDPHelperPortCtrlTable=_SwUDPHelperPortCtrlTable_Object((1,3,6,1,4,1,171,12,99,1,2))
if mibBuilder.loadTexts:swUDPHelperPortCtrlTable.setStatus(_A)
_SwUDPHelperPortCtrlEntry_Object=MibTableRow
swUDPHelperPortCtrlEntry=_SwUDPHelperPortCtrlEntry_Object((1,3,6,1,4,1,171,12,99,1,2,1))
swUDPHelperPortCtrlEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:swUDPHelperPortCtrlEntry.setStatus(_A)
_SwUDPHelperPortNumber_Type=Integer32
_SwUDPHelperPortNumber_Object=MibTableColumn
swUDPHelperPortNumber=_SwUDPHelperPortNumber_Object((1,3,6,1,4,1,171,12,99,1,2,1,1),_SwUDPHelperPortNumber_Type())
swUDPHelperPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:swUDPHelperPortNumber.setStatus(_A)
_SwUDPHelperPortCtrlRowStatus_Type=RowStatus
_SwUDPHelperPortCtrlRowStatus_Object=MibTableColumn
swUDPHelperPortCtrlRowStatus=_SwUDPHelperPortCtrlRowStatus_Object((1,3,6,1,4,1,171,12,99,1,2,1,2),_SwUDPHelperPortCtrlRowStatus_Type())
swUDPHelperPortCtrlRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:swUDPHelperPortCtrlRowStatus.setStatus(_A)
_SwUDPHelperServerCtrlTable_Object=MibTable
swUDPHelperServerCtrlTable=_SwUDPHelperServerCtrlTable_Object((1,3,6,1,4,1,171,12,99,1,3))
if mibBuilder.loadTexts:swUDPHelperServerCtrlTable.setStatus(_A)
_SwUDPHelperServerCtrlEntry_Object=MibTableRow
swUDPHelperServerCtrlEntry=_SwUDPHelperServerCtrlEntry_Object((1,3,6,1,4,1,171,12,99,1,3,1))
swUDPHelperServerCtrlEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:swUDPHelperServerCtrlEntry.setStatus(_A)
class _SwUDPHelperServerCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwUDPHelperServerCtrlInterfaceName_Type.__name__=_E
_SwUDPHelperServerCtrlInterfaceName_Object=MibTableColumn
swUDPHelperServerCtrlInterfaceName=_SwUDPHelperServerCtrlInterfaceName_Object((1,3,6,1,4,1,171,12,99,1,3,1,1),_SwUDPHelperServerCtrlInterfaceName_Type())
swUDPHelperServerCtrlInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:swUDPHelperServerCtrlInterfaceName.setStatus(_A)
_SwUDPHelperServerCtrlServer_Type=IpAddress
_SwUDPHelperServerCtrlServer_Object=MibTableColumn
swUDPHelperServerCtrlServer=_SwUDPHelperServerCtrlServer_Object((1,3,6,1,4,1,171,12,99,1,3,1,2),_SwUDPHelperServerCtrlServer_Type())
swUDPHelperServerCtrlServer.setMaxAccess(_C)
if mibBuilder.loadTexts:swUDPHelperServerCtrlServer.setStatus(_A)
_SwUDPHelperServerCtrlRowStatus_Type=RowStatus
_SwUDPHelperServerCtrlRowStatus_Object=MibTableColumn
swUDPHelperServerCtrlRowStatus=_SwUDPHelperServerCtrlRowStatus_Object((1,3,6,1,4,1,171,12,99,1,3,1,3),_SwUDPHelperServerCtrlRowStatus_Type())
swUDPHelperServerCtrlRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:swUDPHelperServerCtrlRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'swUDPHelperMIB':swUDPHelperMIB,'swUDPHelperMIBObjects':swUDPHelperMIBObjects,'swUDPHelperGeneralGroup':swUDPHelperGeneralGroup,'swUDPHelperState':swUDPHelperState,'swUDPHelperPortCtrlTable':swUDPHelperPortCtrlTable,'swUDPHelperPortCtrlEntry':swUDPHelperPortCtrlEntry,_F:swUDPHelperPortNumber,'swUDPHelperPortCtrlRowStatus':swUDPHelperPortCtrlRowStatus,'swUDPHelperServerCtrlTable':swUDPHelperServerCtrlTable,'swUDPHelperServerCtrlEntry':swUDPHelperServerCtrlEntry,_H:swUDPHelperServerCtrlInterfaceName,_I:swUDPHelperServerCtrlServer,'swUDPHelperServerCtrlRowStatus':swUDPHelperServerCtrlRowStatus})