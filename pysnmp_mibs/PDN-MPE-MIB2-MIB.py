_H='NotificationType'
_G='Integer32'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='read-write'
_C='read-only'
_B='DisplayString'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
mpe_mib2,=mibBuilder.importSymbols('PDN-HEADER-MIB','mpe-mib2')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier',_H,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_H,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','TextualConvention')
_MpeMib2MIBObjects_ObjectIdentity=ObjectIdentity
mpeMib2MIBObjects=_MpeMib2MIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,4,1))
_MpeSystem_ObjectIdentity=ObjectIdentity
mpeSystem=_MpeSystem_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,4,1,1))
_MpeSystemsTable_Object=MibTable
mpeSystemsTable=_MpeSystemsTable_Object((1,3,6,1,4,1,1795,2,24,12,4,1,1,1))
if mibBuilder.loadTexts:mpeSystemsTable.setStatus(_A)
_MpeSystemsEntry_Object=MibTableRow
mpeSystemsEntry=_MpeSystemsEntry_Object((1,3,6,1,4,1,1795,2,24,12,4,1,1,1,1))
mpeSystemsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:mpeSystemsEntry.setStatus(_A)
class _MpeSysDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpeSysDescr_Type.__name__=_B
_MpeSysDescr_Object=MibTableColumn
mpeSysDescr=_MpeSysDescr_Object((1,3,6,1,4,1,1795,2,24,12,4,1,1,1,1,1),_MpeSysDescr_Type())
mpeSysDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:mpeSysDescr.setStatus(_A)
_MpeSysObjectID_Type=ObjectIdentifier
_MpeSysObjectID_Object=MibTableColumn
mpeSysObjectID=_MpeSysObjectID_Object((1,3,6,1,4,1,1795,2,24,12,4,1,1,1,1,2),_MpeSysObjectID_Type())
mpeSysObjectID.setMaxAccess(_C)
if mibBuilder.loadTexts:mpeSysObjectID.setStatus(_A)
_MpeSysUpTime_Type=TimeTicks
_MpeSysUpTime_Object=MibTableColumn
mpeSysUpTime=_MpeSysUpTime_Object((1,3,6,1,4,1,1795,2,24,12,4,1,1,1,1,3),_MpeSysUpTime_Type())
mpeSysUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mpeSysUpTime.setStatus(_A)
class _MpeSysContact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpeSysContact_Type.__name__=_B
_MpeSysContact_Object=MibTableColumn
mpeSysContact=_MpeSysContact_Object((1,3,6,1,4,1,1795,2,24,12,4,1,1,1,1,4),_MpeSysContact_Type())
mpeSysContact.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeSysContact.setStatus(_A)
class _MpeSysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpeSysName_Type.__name__=_B
_MpeSysName_Object=MibTableColumn
mpeSysName=_MpeSysName_Object((1,3,6,1,4,1,1795,2,24,12,4,1,1,1,1,5),_MpeSysName_Type())
mpeSysName.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeSysName.setStatus(_A)
class _MpeSysLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpeSysLocation_Type.__name__=_B
_MpeSysLocation_Object=MibTableColumn
mpeSysLocation=_MpeSysLocation_Object((1,3,6,1,4,1,1795,2,24,12,4,1,1,1,1,6),_MpeSysLocation_Type())
mpeSysLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:mpeSysLocation.setStatus(_A)
class _MpeSysServices_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_MpeSysServices_Type.__name__=_G
_MpeSysServices_Object=MibTableColumn
mpeSysServices=_MpeSysServices_Object((1,3,6,1,4,1,1795,2,24,12,4,1,1,1,1,7),_MpeSysServices_Type())
mpeSysServices.setMaxAccess(_C)
if mibBuilder.loadTexts:mpeSysServices.setStatus(_A)
_MpeMib2MIBTraps_ObjectIdentity=ObjectIdentity
mpeMib2MIBTraps=_MpeMib2MIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,4,2))
mibBuilder.exportSymbols('PDN-MPE-MIB2-MIB',**{'mpeMib2MIBObjects':mpeMib2MIBObjects,'mpeSystem':mpeSystem,'mpeSystemsTable':mpeSystemsTable,'mpeSystemsEntry':mpeSystemsEntry,'mpeSysDescr':mpeSysDescr,'mpeSysObjectID':mpeSysObjectID,'mpeSysUpTime':mpeSysUpTime,'mpeSysContact':mpeSysContact,'mpeSysName':mpeSysName,'mpeSysLocation':mpeSysLocation,'mpeSysServices':mpeSysServices,'mpeMib2MIBTraps':mpeMib2MIBTraps})