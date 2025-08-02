_H='disabled'
_G='enabled'
_F='read-only'
_E='qtechEEEifIndex'
_D='QTECH-EEE-MIB'
_C='2012-10-16 00:00'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechEEEMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,119))
if mibBuilder.loadTexts:qtechEEEMIB.setRevisions((_C,_C))
_QtechEEEConfigMIBObjects_ObjectIdentity=ObjectIdentity
qtechEEEConfigMIBObjects=_QtechEEEConfigMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,119,1))
_QtechEEETable_Object=MibTable
qtechEEETable=_QtechEEETable_Object((1,3,6,1,4,1,27514,1,1,10,2,119,1,1))
if mibBuilder.loadTexts:qtechEEETable.setStatus(_A)
_QtechEEEEntry_Object=MibTableRow
qtechEEEEntry=_QtechEEEEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,119,1,1,1))
qtechEEEEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:qtechEEEEntry.setStatus(_A)
class _QtechEEEifIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_QtechEEEifIndex_Type.__name__=_B
_QtechEEEifIndex_Object=MibTableColumn
qtechEEEifIndex=_QtechEEEifIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,119,1,1,1,1),_QtechEEEifIndex_Type())
qtechEEEifIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechEEEifIndex.setStatus(_A)
class _QtechEEEAdminEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_QtechEEEAdminEnable_Type.__name__=_B
_QtechEEEAdminEnable_Object=MibTableColumn
qtechEEEAdminEnable=_QtechEEEAdminEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,119,1,1,1,2),_QtechEEEAdminEnable_Type())
qtechEEEAdminEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:qtechEEEAdminEnable.setStatus(_A)
class _QtechEEEOperEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_QtechEEEOperEnable_Type.__name__=_B
_QtechEEEOperEnable_Object=MibTableColumn
qtechEEEOperEnable=_QtechEEEOperEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,119,1,1,1,3),_QtechEEEOperEnable_Type())
qtechEEEOperEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechEEEOperEnable.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'qtechEEEMIB':qtechEEEMIB,'qtechEEEConfigMIBObjects':qtechEEEConfigMIBObjects,'qtechEEETable':qtechEEETable,'qtechEEEEntry':qtechEEEEntry,_E:qtechEEEifIndex,'qtechEEEAdminEnable':qtechEEEAdminEnable,'qtechEEEOperEnable':qtechEEEOperEnable})