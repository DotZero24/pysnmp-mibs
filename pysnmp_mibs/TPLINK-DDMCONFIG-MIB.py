_H='read-write'
_G='read-only'
_F='DisplayString'
_E='ifIndex'
_D='IF-MIB'
_C='OctetString'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
tplinkDdmManageMIBObjects,=mibBuilder.importSymbols('TPLINK-DDMMANAGE-MIB','tplinkDdmManageMIBObjects')
ddmConfig=ModuleIdentity((1,3,6,1,4,1,11863,6,96,1,1))
if mibBuilder.loadTexts:ddmConfig.setRevisions(('2009-08-27 00:00',))
_DdmConfigTable_Object=MibTable
ddmConfigTable=_DdmConfigTable_Object((1,3,6,1,4,1,11863,6,96,1,1,1))
if mibBuilder.loadTexts:ddmConfigTable.setStatus(_A)
_DdmConfigEntry_Object=MibTableRow
ddmConfigEntry=_DdmConfigEntry_Object((1,3,6,1,4,1,11863,6,96,1,1,1,1))
ddmConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ddmConfigEntry.setStatus(_A)
class _DdmConfigPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DdmConfigPort_Type.__name__=_F
_DdmConfigPort_Object=MibTableColumn
ddmConfigPort=_DdmConfigPort_Object((1,3,6,1,4,1,11863,6,96,1,1,1,1,1),_DdmConfigPort_Type())
ddmConfigPort.setMaxAccess(_G)
if mibBuilder.loadTexts:ddmConfigPort.setStatus(_A)
class _DdmConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_DdmConfigStatus_Type.__name__=_B
_DdmConfigStatus_Object=MibTableColumn
ddmConfigStatus=_DdmConfigStatus_Object((1,3,6,1,4,1,11863,6,96,1,1,1,1,2),_DdmConfigStatus_Type())
ddmConfigStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:ddmConfigStatus.setStatus(_A)
class _DdmConfigShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('warning',1),('alarm',2)))
_DdmConfigShutdown_Type.__name__=_B
_DdmConfigShutdown_Object=MibTableColumn
ddmConfigShutdown=_DdmConfigShutdown_Object((1,3,6,1,4,1,11863,6,96,1,1,1,1,3),_DdmConfigShutdown_Type())
ddmConfigShutdown.setMaxAccess(_H)
if mibBuilder.loadTexts:ddmConfigShutdown.setStatus(_A)
class _DdmConfigPortLAG_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_DdmConfigPortLAG_Type.__name__=_C
_DdmConfigPortLAG_Object=MibTableColumn
ddmConfigPortLAG=_DdmConfigPortLAG_Object((1,3,6,1,4,1,11863,6,96,1,1,1,1,4),_DdmConfigPortLAG_Type())
ddmConfigPortLAG.setMaxAccess(_G)
if mibBuilder.loadTexts:ddmConfigPortLAG.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-DDMCONFIG-MIB',**{'ddmConfig':ddmConfig,'ddmConfigTable':ddmConfigTable,'ddmConfigEntry':ddmConfigEntry,'ddmConfigPort':ddmConfigPort,'ddmConfigStatus':ddmConfigStatus,'ddmConfigShutdown':ddmConfigShutdown,'ddmConfigPortLAG':ddmConfigPortLAG})