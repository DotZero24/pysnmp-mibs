_F='nsZoneCfgId'
_E='NETSCREEN-ZONE-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenZone,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenZone')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
netscreenZoneMibModule=ModuleIdentity((1,3,6,1,4,1,3224,8,0))
if mibBuilder.loadTexts:netscreenZoneMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-13 00:00','2001-09-28 00:00','2000-05-08 00:00'))
_NsZoneCfg_ObjectIdentity=ObjectIdentity
nsZoneCfg=_NsZoneCfg_ObjectIdentity((1,3,6,1,4,1,3224,8,1))
_NsZoneCfgTable_Object=MibTable
nsZoneCfgTable=_NsZoneCfgTable_Object((1,3,6,1,4,1,3224,8,1,1))
if mibBuilder.loadTexts:nsZoneCfgTable.setStatus(_A)
_NsZoneCfgEntry_Object=MibTableRow
nsZoneCfgEntry=_NsZoneCfgEntry_Object((1,3,6,1,4,1,3224,8,1,1,1))
nsZoneCfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nsZoneCfgEntry.setStatus(_A)
class _NsZoneCfgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsZoneCfgId_Type.__name__=_C
_NsZoneCfgId_Object=MibTableColumn
nsZoneCfgId=_NsZoneCfgId_Object((1,3,6,1,4,1,3224,8,1,1,1,1),_NsZoneCfgId_Type())
nsZoneCfgId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsZoneCfgId.setStatus(_A)
class _NsZoneCfgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsZoneCfgName_Type.__name__=_D
_NsZoneCfgName_Object=MibTableColumn
nsZoneCfgName=_NsZoneCfgName_Object((1,3,6,1,4,1,3224,8,1,1,1,2),_NsZoneCfgName_Type())
nsZoneCfgName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsZoneCfgName.setStatus(_A)
class _NsZoneCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('regular',0),('layer2',1),('tunnel',2),('null',3),('func',4)))
_NsZoneCfgType_Type.__name__=_C
_NsZoneCfgType_Object=MibTableColumn
nsZoneCfgType=_NsZoneCfgType_Object((1,3,6,1,4,1,3224,8,1,1,1,3),_NsZoneCfgType_Type())
nsZoneCfgType.setMaxAccess(_B)
if mibBuilder.loadTexts:nsZoneCfgType.setStatus(_A)
_NsZoneCfgVsys_Type=Integer32
_NsZoneCfgVsys_Object=MibTableColumn
nsZoneCfgVsys=_NsZoneCfgVsys_Object((1,3,6,1,4,1,3224,8,1,1,1,4),_NsZoneCfgVsys_Type())
nsZoneCfgVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsZoneCfgVsys.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'netscreenZoneMibModule':netscreenZoneMibModule,'nsZoneCfg':nsZoneCfg,'nsZoneCfgTable':nsZoneCfgTable,'nsZoneCfgEntry':nsZoneCfgEntry,_F:nsZoneCfgId,'nsZoneCfgName':nsZoneCfgName,'nsZoneCfgType':nsZoneCfgType,'nsZoneCfgVsys':nsZoneCfgVsys})