_H='zxr10IPSecondaryAddr'
_G='ZXR10-IP-IF-MIB'
_F='read-only'
_E='ifIndex'
_D='IF-MIB'
_C='DisplayString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
zxr10interfaces,=mibBuilder.importSymbols('ZXR10-SMI','zxr10interfaces')
zxr10IPIfMIB=ModuleIdentity((1,3,6,1,4,1,3902,3,103,1))
if mibBuilder.loadTexts:zxr10IPIfMIB.setRevisions(('2005-04-12 00:00',))
class DisplayString(OctetString):0
_Zxr10IPIfMIBObjects_ObjectIdentity=ObjectIdentity
zxr10IPIfMIBObjects=_Zxr10IPIfMIBObjects_ObjectIdentity((1,3,6,1,4,1,3902,3,103,1,1))
_Zxr10IPAddressConfiguration_ObjectIdentity=ObjectIdentity
zxr10IPAddressConfiguration=_Zxr10IPAddressConfiguration_ObjectIdentity((1,3,6,1,4,1,3902,3,103,1,1,1))
_Zxr10IPAddrTable_Object=MibTable
zxr10IPAddrTable=_Zxr10IPAddrTable_Object((1,3,6,1,4,1,3902,3,103,1,1,1,1))
if mibBuilder.loadTexts:zxr10IPAddrTable.setStatus(_A)
_Zxr10IPAddrEntry_Object=MibTableRow
zxr10IPAddrEntry=_Zxr10IPAddrEntry_Object((1,3,6,1,4,1,3902,3,103,1,1,1,1,1))
zxr10IPAddrEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxr10IPAddrEntry.setStatus(_A)
_Zxr10IPAddrPrimaryIp_Type=IpAddress
_Zxr10IPAddrPrimaryIp_Object=MibTableColumn
zxr10IPAddrPrimaryIp=_Zxr10IPAddrPrimaryIp_Object((1,3,6,1,4,1,3902,3,103,1,1,1,1,1,1),_Zxr10IPAddrPrimaryIp_Type())
zxr10IPAddrPrimaryIp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10IPAddrPrimaryIp.setStatus(_A)
_Zxr10IPAddrPrimaryIpMask_Type=IpAddress
_Zxr10IPAddrPrimaryIpMask_Object=MibTableColumn
zxr10IPAddrPrimaryIpMask=_Zxr10IPAddrPrimaryIpMask_Object((1,3,6,1,4,1,3902,3,103,1,1,1,1,1,2),_Zxr10IPAddrPrimaryIpMask_Type())
zxr10IPAddrPrimaryIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10IPAddrPrimaryIpMask.setStatus(_A)
_Zxr10IPAddrBroadcast_Type=IpAddress
_Zxr10IPAddrBroadcast_Object=MibTableColumn
zxr10IPAddrBroadcast=_Zxr10IPAddrBroadcast_Object((1,3,6,1,4,1,3902,3,103,1,1,1,1,1,3),_Zxr10IPAddrBroadcast_Type())
zxr10IPAddrBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10IPAddrBroadcast.setStatus(_A)
_Zxr10IPAddrRowStatus_Type=RowStatus
_Zxr10IPAddrRowStatus_Object=MibTableColumn
zxr10IPAddrRowStatus=_Zxr10IPAddrRowStatus_Object((1,3,6,1,4,1,3902,3,103,1,1,1,1,1,4),_Zxr10IPAddrRowStatus_Type())
zxr10IPAddrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10IPAddrRowStatus.setStatus(_A)
class _Zxr10IPAddrIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10IPAddrIfName_Type.__name__=_C
_Zxr10IPAddrIfName_Object=MibTableColumn
zxr10IPAddrIfName=_Zxr10IPAddrIfName_Object((1,3,6,1,4,1,3902,3,103,1,1,1,1,1,5),_Zxr10IPAddrIfName_Type())
zxr10IPAddrIfName.setMaxAccess(_F)
if mibBuilder.loadTexts:zxr10IPAddrIfName.setStatus(_A)
_Zxr10IPSecondaryAddrTable_Object=MibTable
zxr10IPSecondaryAddrTable=_Zxr10IPSecondaryAddrTable_Object((1,3,6,1,4,1,3902,3,103,1,1,1,2))
if mibBuilder.loadTexts:zxr10IPSecondaryAddrTable.setStatus(_A)
_Zxr10IPSecondaryAddrEnry_Object=MibTableRow
zxr10IPSecondaryAddrEnry=_Zxr10IPSecondaryAddrEnry_Object((1,3,6,1,4,1,3902,3,103,1,1,1,2,1))
zxr10IPSecondaryAddrEnry.setIndexNames((0,_D,_E),(0,_G,_H))
if mibBuilder.loadTexts:zxr10IPSecondaryAddrEnry.setStatus(_A)
_Zxr10IPSecondaryAddr_Type=IpAddress
_Zxr10IPSecondaryAddr_Object=MibTableColumn
zxr10IPSecondaryAddr=_Zxr10IPSecondaryAddr_Object((1,3,6,1,4,1,3902,3,103,1,1,1,2,1,1),_Zxr10IPSecondaryAddr_Type())
zxr10IPSecondaryAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10IPSecondaryAddr.setStatus(_A)
_Zxr10IPSecondaryAddrMask_Type=IpAddress
_Zxr10IPSecondaryAddrMask_Object=MibTableColumn
zxr10IPSecondaryAddrMask=_Zxr10IPSecondaryAddrMask_Object((1,3,6,1,4,1,3902,3,103,1,1,1,2,1,2),_Zxr10IPSecondaryAddrMask_Type())
zxr10IPSecondaryAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10IPSecondaryAddrMask.setStatus(_A)
_Zxr10IPSecondaryAddrRowStatus_Type=RowStatus
_Zxr10IPSecondaryAddrRowStatus_Object=MibTableColumn
zxr10IPSecondaryAddrRowStatus=_Zxr10IPSecondaryAddrRowStatus_Object((1,3,6,1,4,1,3902,3,103,1,1,1,2,1,3),_Zxr10IPSecondaryAddrRowStatus_Type())
zxr10IPSecondaryAddrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10IPSecondaryAddrRowStatus.setStatus(_A)
class _Zxr10IPSecondaryIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10IPSecondaryIfName_Type.__name__=_C
_Zxr10IPSecondaryIfName_Object=MibTableColumn
zxr10IPSecondaryIfName=_Zxr10IPSecondaryIfName_Object((1,3,6,1,4,1,3902,3,103,1,1,1,2,1,4),_Zxr10IPSecondaryIfName_Type())
zxr10IPSecondaryIfName.setMaxAccess(_F)
if mibBuilder.loadTexts:zxr10IPSecondaryIfName.setStatus(_A)
mibBuilder.exportSymbols(_G,**{_C:DisplayString,'zxr10IPIfMIB':zxr10IPIfMIB,'zxr10IPIfMIBObjects':zxr10IPIfMIBObjects,'zxr10IPAddressConfiguration':zxr10IPAddressConfiguration,'zxr10IPAddrTable':zxr10IPAddrTable,'zxr10IPAddrEntry':zxr10IPAddrEntry,'zxr10IPAddrPrimaryIp':zxr10IPAddrPrimaryIp,'zxr10IPAddrPrimaryIpMask':zxr10IPAddrPrimaryIpMask,'zxr10IPAddrBroadcast':zxr10IPAddrBroadcast,'zxr10IPAddrRowStatus':zxr10IPAddrRowStatus,'zxr10IPAddrIfName':zxr10IPAddrIfName,'zxr10IPSecondaryAddrTable':zxr10IPSecondaryAddrTable,'zxr10IPSecondaryAddrEnry':zxr10IPSecondaryAddrEnry,_H:zxr10IPSecondaryAddr,'zxr10IPSecondaryAddrMask':zxr10IPSecondaryAddrMask,'zxr10IPSecondaryAddrRowStatus':zxr10IPSecondaryAddrRowStatus,'zxr10IPSecondaryIfName':zxr10IPSecondaryIfName})