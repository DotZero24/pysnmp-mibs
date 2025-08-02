_F='zyPrivateVlanType'
_E='ZYXEL-PRIVATE-VLAN-MIB'
_D='Integer32'
_C='read-write'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelPrivateVlan=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,68))
_ZyxelPrivateVlanSetup_ObjectIdentity=ObjectIdentity
zyxelPrivateVlanSetup=_ZyxelPrivateVlanSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,68,1))
_ZyxelPrivateVlanTable_Object=MibTable
zyxelPrivateVlanTable=_ZyxelPrivateVlanTable_Object((1,3,6,1,4,1,890,1,15,3,68,1,1))
if mibBuilder.loadTexts:zyxelPrivateVlanTable.setStatus(_A)
_ZyxelPrivateVlanEntry_Object=MibTableRow
zyxelPrivateVlanEntry=_ZyxelPrivateVlanEntry_Object((1,3,6,1,4,1,890,1,15,3,68,1,1,1))
zyxelPrivateVlanEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zyxelPrivateVlanEntry.setStatus(_A)
class _ZyPrivateVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('normal',0),('primary',1),('isolated',2),('community',3)))
_ZyPrivateVlanType_Type.__name__=_D
_ZyPrivateVlanType_Object=MibTableColumn
zyPrivateVlanType=_ZyPrivateVlanType_Object((1,3,6,1,4,1,890,1,15,3,68,1,1,1,1),_ZyPrivateVlanType_Type())
zyPrivateVlanType.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPrivateVlanType.setStatus(_A)
class _ZyPrivateVlanAssociatedVlanMap1k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyPrivateVlanAssociatedVlanMap1k_Type.__name__=_B
_ZyPrivateVlanAssociatedVlanMap1k_Object=MibTableColumn
zyPrivateVlanAssociatedVlanMap1k=_ZyPrivateVlanAssociatedVlanMap1k_Object((1,3,6,1,4,1,890,1,15,3,68,1,1,1,2),_ZyPrivateVlanAssociatedVlanMap1k_Type())
zyPrivateVlanAssociatedVlanMap1k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPrivateVlanAssociatedVlanMap1k.setStatus(_A)
class _ZyPrivateVlanAssociatedVlanMap2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyPrivateVlanAssociatedVlanMap2k_Type.__name__=_B
_ZyPrivateVlanAssociatedVlanMap2k_Object=MibTableColumn
zyPrivateVlanAssociatedVlanMap2k=_ZyPrivateVlanAssociatedVlanMap2k_Object((1,3,6,1,4,1,890,1,15,3,68,1,1,1,3),_ZyPrivateVlanAssociatedVlanMap2k_Type())
zyPrivateVlanAssociatedVlanMap2k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPrivateVlanAssociatedVlanMap2k.setStatus(_A)
class _ZyPrivateVlanAssociatedVlanMap3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyPrivateVlanAssociatedVlanMap3k_Type.__name__=_B
_ZyPrivateVlanAssociatedVlanMap3k_Object=MibTableColumn
zyPrivateVlanAssociatedVlanMap3k=_ZyPrivateVlanAssociatedVlanMap3k_Object((1,3,6,1,4,1,890,1,15,3,68,1,1,1,4),_ZyPrivateVlanAssociatedVlanMap3k_Type())
zyPrivateVlanAssociatedVlanMap3k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPrivateVlanAssociatedVlanMap3k.setStatus(_A)
class _ZyPrivateVlanAssociatedVlanMap4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyPrivateVlanAssociatedVlanMap4k_Type.__name__=_B
_ZyPrivateVlanAssociatedVlanMap4k_Object=MibTableColumn
zyPrivateVlanAssociatedVlanMap4k=_ZyPrivateVlanAssociatedVlanMap4k_Object((1,3,6,1,4,1,890,1,15,3,68,1,1,1,5),_ZyPrivateVlanAssociatedVlanMap4k_Type())
zyPrivateVlanAssociatedVlanMap4k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPrivateVlanAssociatedVlanMap4k.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zyxelPrivateVlan':zyxelPrivateVlan,'zyxelPrivateVlanSetup':zyxelPrivateVlanSetup,'zyxelPrivateVlanTable':zyxelPrivateVlanTable,'zyxelPrivateVlanEntry':zyxelPrivateVlanEntry,_F:zyPrivateVlanType,'zyPrivateVlanAssociatedVlanMap1k':zyPrivateVlanAssociatedVlanMap1k,'zyPrivateVlanAssociatedVlanMap2k':zyPrivateVlanAssociatedVlanMap2k,'zyPrivateVlanAssociatedVlanMap3k':zyPrivateVlanAssociatedVlanMap3k,'zyPrivateVlanAssociatedVlanMap4k':zyPrivateVlanAssociatedVlanMap4k})