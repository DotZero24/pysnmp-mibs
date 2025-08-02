_K='read-only'
_J='hpnicfObjpZonePairRuleID'
_I='hpnicfObjpZonePairIPVersion'
_H='hpnicfObjpZonePairDstZone'
_G='hpnicfObjpZonePairSrcZone'
_F='Unsigned32'
_E='Integer32'
_D='OctetString'
_C='not-accessible'
_B='HPN-ICF-OBJP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfObjp=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,155))
if mibBuilder.loadTexts:hpnicfObjp.setRevisions(('2014-03-10 15:36',))
_HpnicfObjpZonePairObjects_ObjectIdentity=ObjectIdentity
hpnicfObjpZonePairObjects=_HpnicfObjpZonePairObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,155,1))
_HpnicfObjpZonePairRunningInfoTable_Object=MibTable
hpnicfObjpZonePairRunningInfoTable=_HpnicfObjpZonePairRunningInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,155,1,1))
if mibBuilder.loadTexts:hpnicfObjpZonePairRunningInfoTable.setStatus(_A)
_HpnicfObjpZonePairRunningInfoEntry_Object=MibTableRow
hpnicfObjpZonePairRunningInfoEntry=_HpnicfObjpZonePairRunningInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,155,1,1,1))
hpnicfObjpZonePairRunningInfoEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:hpnicfObjpZonePairRunningInfoEntry.setStatus(_A)
class _HpnicfObjpZonePairSrcZone_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfObjpZonePairSrcZone_Type.__name__=_D
_HpnicfObjpZonePairSrcZone_Object=MibTableColumn
hpnicfObjpZonePairSrcZone=_HpnicfObjpZonePairSrcZone_Object((1,3,6,1,4,1,11,2,14,11,15,2,155,1,1,1,1),_HpnicfObjpZonePairSrcZone_Type())
hpnicfObjpZonePairSrcZone.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfObjpZonePairSrcZone.setStatus(_A)
class _HpnicfObjpZonePairDstZone_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfObjpZonePairDstZone_Type.__name__=_D
_HpnicfObjpZonePairDstZone_Object=MibTableColumn
hpnicfObjpZonePairDstZone=_HpnicfObjpZonePairDstZone_Object((1,3,6,1,4,1,11,2,14,11,15,2,155,1,1,1,2),_HpnicfObjpZonePairDstZone_Type())
hpnicfObjpZonePairDstZone.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfObjpZonePairDstZone.setStatus(_A)
class _HpnicfObjpZonePairIPVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_HpnicfObjpZonePairIPVersion_Type.__name__=_E
_HpnicfObjpZonePairIPVersion_Object=MibTableColumn
hpnicfObjpZonePairIPVersion=_HpnicfObjpZonePairIPVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,155,1,1,1,3),_HpnicfObjpZonePairIPVersion_Type())
hpnicfObjpZonePairIPVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfObjpZonePairIPVersion.setStatus(_A)
class _HpnicfObjpZonePairRuleID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_HpnicfObjpZonePairRuleID_Type.__name__=_F
_HpnicfObjpZonePairRuleID_Object=MibTableColumn
hpnicfObjpZonePairRuleID=_HpnicfObjpZonePairRuleID_Object((1,3,6,1,4,1,11,2,14,11,15,2,155,1,1,1,4),_HpnicfObjpZonePairRuleID_Type())
hpnicfObjpZonePairRuleID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfObjpZonePairRuleID.setStatus(_A)
_HpnicfObjpZonePairMatchPacketCount_Type=Counter64
_HpnicfObjpZonePairMatchPacketCount_Object=MibTableColumn
hpnicfObjpZonePairMatchPacketCount=_HpnicfObjpZonePairMatchPacketCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,155,1,1,1,5),_HpnicfObjpZonePairMatchPacketCount_Type())
hpnicfObjpZonePairMatchPacketCount.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfObjpZonePairMatchPacketCount.setStatus(_A)
_HpnicfObjpZonePairLastMatchTime_Type=Unsigned32
_HpnicfObjpZonePairLastMatchTime_Object=MibTableColumn
hpnicfObjpZonePairLastMatchTime=_HpnicfObjpZonePairLastMatchTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,155,1,1,1,6),_HpnicfObjpZonePairLastMatchTime_Type())
hpnicfObjpZonePairLastMatchTime.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfObjpZonePairLastMatchTime.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfObjp':hpnicfObjp,'hpnicfObjpZonePairObjects':hpnicfObjpZonePairObjects,'hpnicfObjpZonePairRunningInfoTable':hpnicfObjpZonePairRunningInfoTable,'hpnicfObjpZonePairRunningInfoEntry':hpnicfObjpZonePairRunningInfoEntry,_G:hpnicfObjpZonePairSrcZone,_H:hpnicfObjpZonePairDstZone,_I:hpnicfObjpZonePairIPVersion,_J:hpnicfObjpZonePairRuleID,'hpnicfObjpZonePairMatchPacketCount':hpnicfObjpZonePairMatchPacketCount,'hpnicfObjpZonePairLastMatchTime':hpnicfObjpZonePairLastMatchTime})