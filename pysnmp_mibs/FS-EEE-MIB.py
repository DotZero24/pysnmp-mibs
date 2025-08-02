_H='disabled'
_G='enabled'
_F='read-only'
_E='fsEEEifIndex'
_D='FS-EEE-MIB'
_C='2012-10-16 00:00'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsEEEMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,119))
if mibBuilder.loadTexts:fsEEEMIB.setRevisions((_C,_C))
_FsEEEConfigMIBObjects_ObjectIdentity=ObjectIdentity
fsEEEConfigMIBObjects=_FsEEEConfigMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,119,1))
_FsEEETable_Object=MibTable
fsEEETable=_FsEEETable_Object((1,3,6,1,4,1,52642,1,1,10,2,119,1,1))
if mibBuilder.loadTexts:fsEEETable.setStatus(_A)
_FsEEEEntry_Object=MibTableRow
fsEEEEntry=_FsEEEEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,119,1,1,1))
fsEEEEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fsEEEEntry.setStatus(_A)
class _FsEEEifIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsEEEifIndex_Type.__name__=_B
_FsEEEifIndex_Object=MibTableColumn
fsEEEifIndex=_FsEEEifIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,119,1,1,1,1),_FsEEEifIndex_Type())
fsEEEifIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEEEifIndex.setStatus(_A)
class _FsEEEAdminEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsEEEAdminEnable_Type.__name__=_B
_FsEEEAdminEnable_Object=MibTableColumn
fsEEEAdminEnable=_FsEEEAdminEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,119,1,1,1,2),_FsEEEAdminEnable_Type())
fsEEEAdminEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsEEEAdminEnable.setStatus(_A)
class _FsEEEOperEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsEEEOperEnable_Type.__name__=_B
_FsEEEOperEnable_Object=MibTableColumn
fsEEEOperEnable=_FsEEEOperEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,119,1,1,1,3),_FsEEEOperEnable_Type())
fsEEEOperEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:fsEEEOperEnable.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fsEEEMIB':fsEEEMIB,'fsEEEConfigMIBObjects':fsEEEConfigMIBObjects,'fsEEETable':fsEEETable,'fsEEEEntry':fsEEEEntry,_E:fsEEEifIndex,'fsEEEAdminEnable':fsEEEAdminEnable,'fsEEEOperEnable':fsEEEOperEnable})