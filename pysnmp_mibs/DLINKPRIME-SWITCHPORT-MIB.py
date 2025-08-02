_L='dpSwPortBasicGroup'
_K='dpSwPortIfSpeedAutoDowngrade'
_J='dpSwPortIfJumboFrameSize'
_I='dpSwPortIfMdix'
_H='TruthValue'
_G='Unsigned32'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='DLINKPRIME-SWITCHPORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_H)
dlinkPrimeSwitchPortMIB=ModuleIdentity((1,3,6,1,4,1,171,15,20))
if mibBuilder.loadTexts:dlinkPrimeSwitchPortMIB.setRevisions(('2014-05-07 00:00',))
_DpSwPortNotifications_ObjectIdentity=ObjectIdentity
dpSwPortNotifications=_DpSwPortNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,20,0))
_DpSwPortObjects_ObjectIdentity=ObjectIdentity
dpSwPortObjects=_DpSwPortObjects_ObjectIdentity((1,3,6,1,4,1,171,15,20,1))
_DpSwPortIfTable_Object=MibTable
dpSwPortIfTable=_DpSwPortIfTable_Object((1,3,6,1,4,1,171,15,20,1,1))
if mibBuilder.loadTexts:dpSwPortIfTable.setStatus(_A)
_DpSwPortIfEntry_Object=MibTableRow
dpSwPortIfEntry=_DpSwPortIfEntry_Object((1,3,6,1,4,1,171,15,20,1,1,1))
dpSwPortIfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:dpSwPortIfEntry.setStatus(_A)
class _DpSwPortIfMdix_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('normal',2),('cross',3)))
_DpSwPortIfMdix_Type.__name__=_F
_DpSwPortIfMdix_Object=MibTableColumn
dpSwPortIfMdix=_DpSwPortIfMdix_Object((1,3,6,1,4,1,171,15,20,1,1,1,1),_DpSwPortIfMdix_Type())
dpSwPortIfMdix.setMaxAccess(_C)
if mibBuilder.loadTexts:dpSwPortIfMdix.setStatus(_A)
class _DpSwPortIfJumboFrameSize_Type(Unsigned32):defaultValue=1518
_DpSwPortIfJumboFrameSize_Type.__name__=_G
_DpSwPortIfJumboFrameSize_Object=MibTableColumn
dpSwPortIfJumboFrameSize=_DpSwPortIfJumboFrameSize_Object((1,3,6,1,4,1,171,15,20,1,1,1,2),_DpSwPortIfJumboFrameSize_Type())
dpSwPortIfJumboFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dpSwPortIfJumboFrameSize.setStatus(_A)
class _DpSwPortIfSpeedAutoDowngrade_Type(TruthValue):defaultValue=2
_DpSwPortIfSpeedAutoDowngrade_Type.__name__=_H
_DpSwPortIfSpeedAutoDowngrade_Object=MibTableColumn
dpSwPortIfSpeedAutoDowngrade=_DpSwPortIfSpeedAutoDowngrade_Object((1,3,6,1,4,1,171,15,20,1,1,1,3),_DpSwPortIfSpeedAutoDowngrade_Type())
dpSwPortIfSpeedAutoDowngrade.setMaxAccess(_C)
if mibBuilder.loadTexts:dpSwPortIfSpeedAutoDowngrade.setStatus(_A)
_DpSwPortConformance_ObjectIdentity=ObjectIdentity
dpSwPortConformance=_DpSwPortConformance_ObjectIdentity((1,3,6,1,4,1,171,15,20,2))
_DpSwPortCompliances_ObjectIdentity=ObjectIdentity
dpSwPortCompliances=_DpSwPortCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,20,2,1))
_DpSwPortGroups_ObjectIdentity=ObjectIdentity
dpSwPortGroups=_DpSwPortGroups_ObjectIdentity((1,3,6,1,4,1,171,15,20,2,2))
dpSwPortBasicGroup=ObjectGroup((1,3,6,1,4,1,171,15,20,2,2,1))
dpSwPortBasicGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:dpSwPortBasicGroup.setStatus(_A)
dpSwPortCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,20,2,1,1))
dpSwPortCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:dpSwPortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimeSwitchPortMIB':dlinkPrimeSwitchPortMIB,'dpSwPortNotifications':dpSwPortNotifications,'dpSwPortObjects':dpSwPortObjects,'dpSwPortIfTable':dpSwPortIfTable,'dpSwPortIfEntry':dpSwPortIfEntry,_I:dpSwPortIfMdix,_J:dpSwPortIfJumboFrameSize,_K:dpSwPortIfSpeedAutoDowngrade,'dpSwPortConformance':dpSwPortConformance,'dpSwPortCompliances':dpSwPortCompliances,'dpSwPortCompliance':dpSwPortCompliance,'dpSwPortGroups':dpSwPortGroups,_L:dpSwPortBasicGroup})