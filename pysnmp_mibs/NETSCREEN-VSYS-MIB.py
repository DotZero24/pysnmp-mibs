_F='read-only'
_E='nsVsysCfgId'
_D='NETSCREEN-VSYS-MIB'
_C='DisplayString'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVsys,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVsys')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
netscreenVsysMibModule=ModuleIdentity((1,3,6,1,4,1,3224,15,0))
if mibBuilder.loadTexts:netscreenVsysMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-13 00:00','2001-09-28 00:00','2000-05-08 00:00'))
_NsVsysCfg_ObjectIdentity=ObjectIdentity
nsVsysCfg=_NsVsysCfg_ObjectIdentity((1,3,6,1,4,1,3224,15,1))
_NsVsysCfgTable_Object=MibTable
nsVsysCfgTable=_NsVsysCfgTable_Object((1,3,6,1,4,1,3224,15,1,1))
if mibBuilder.loadTexts:nsVsysCfgTable.setStatus(_A)
_NsVsysCfgEntry_Object=MibTableRow
nsVsysCfgEntry=_NsVsysCfgEntry_Object((1,3,6,1,4,1,3224,15,1,1,1))
nsVsysCfgEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:nsVsysCfgEntry.setStatus(_A)
class _NsVsysCfgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsVsysCfgId_Type.__name__=_B
_NsVsysCfgId_Object=MibTableColumn
nsVsysCfgId=_NsVsysCfgId_Object((1,3,6,1,4,1,3224,15,1,1,1,1),_NsVsysCfgId_Type())
nsVsysCfgId.setMaxAccess(_F)
if mibBuilder.loadTexts:nsVsysCfgId.setStatus(_A)
class _NsVsysCfgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsVsysCfgName_Type.__name__=_C
_NsVsysCfgName_Object=MibTableColumn
nsVsysCfgName=_NsVsysCfgName_Object((1,3,6,1,4,1,3224,15,1,1,1,2),_NsVsysCfgName_Type())
nsVsysCfgName.setMaxAccess(_F)
if mibBuilder.loadTexts:nsVsysCfgName.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'netscreenVsysMibModule':netscreenVsysMibModule,'nsVsysCfg':nsVsysCfg,'nsVsysCfgTable':nsVsysCfgTable,'nsVsysCfgEntry':nsVsysCfgEntry,_E:nsVsysCfgId,'nsVsysCfgName':nsVsysCfgName})