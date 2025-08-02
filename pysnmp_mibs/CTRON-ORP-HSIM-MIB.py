_F='ctOrpHSIMIndex'
_E='ctOrpHSIMSlot'
_D='CTRON-ORP-HSIM-MIB'
_C='read-only'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctOrpHSIM,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctOrpHSIM')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CtOrpHSIMTable_Object=MibTable
ctOrpHSIMTable=_CtOrpHSIMTable_Object((1,3,6,1,4,1,52,4,1,1,15,1))
if mibBuilder.loadTexts:ctOrpHSIMTable.setStatus(_A)
_CtOrpHSIMEntry_Object=MibTableRow
ctOrpHSIMEntry=_CtOrpHSIMEntry_Object((1,3,6,1,4,1,52,4,1,1,15,1,1))
ctOrpHSIMEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:ctOrpHSIMEntry.setStatus(_A)
_CtOrpHSIMSlot_Type=Integer32
_CtOrpHSIMSlot_Object=MibTableColumn
ctOrpHSIMSlot=_CtOrpHSIMSlot_Object((1,3,6,1,4,1,52,4,1,1,15,1,1,1),_CtOrpHSIMSlot_Type())
ctOrpHSIMSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:ctOrpHSIMSlot.setStatus(_A)
_CtOrpHSIMIndex_Type=Integer32
_CtOrpHSIMIndex_Object=MibTableColumn
ctOrpHSIMIndex=_CtOrpHSIMIndex_Object((1,3,6,1,4,1,52,4,1,1,15,1,1,2),_CtOrpHSIMIndex_Type())
ctOrpHSIMIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctOrpHSIMIndex.setStatus(_A)
_CtOrpHSIMIfRef_Type=ObjectIdentifier
_CtOrpHSIMIfRef_Object=MibTableColumn
ctOrpHSIMIfRef=_CtOrpHSIMIfRef_Object((1,3,6,1,4,1,52,4,1,1,15,1,1,3),_CtOrpHSIMIfRef_Type())
ctOrpHSIMIfRef.setMaxAccess(_C)
if mibBuilder.loadTexts:ctOrpHSIMIfRef.setStatus(_A)
_CtOrpHSIMMACAddress_Type=MacAddress
_CtOrpHSIMMACAddress_Object=MibTableColumn
ctOrpHSIMMACAddress=_CtOrpHSIMMACAddress_Object((1,3,6,1,4,1,52,4,1,1,15,1,1,4),_CtOrpHSIMMACAddress_Type())
ctOrpHSIMMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctOrpHSIMMACAddress.setStatus(_A)
_CtOrpHSIMIPAddress_Type=IpAddress
_CtOrpHSIMIPAddress_Object=MibTableColumn
ctOrpHSIMIPAddress=_CtOrpHSIMIPAddress_Object((1,3,6,1,4,1,52,4,1,1,15,1,1,5),_CtOrpHSIMIPAddress_Type())
ctOrpHSIMIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ctOrpHSIMIPAddress.setStatus(_A)
_CtOrpHSIMSubnetMask_Type=IpAddress
_CtOrpHSIMSubnetMask_Object=MibTableColumn
ctOrpHSIMSubnetMask=_CtOrpHSIMSubnetMask_Object((1,3,6,1,4,1,52,4,1,1,15,1,1,6),_CtOrpHSIMSubnetMask_Type())
ctOrpHSIMSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ctOrpHSIMSubnetMask.setStatus(_A)
_CtOrpHSIMROCommName_Type=OctetString
_CtOrpHSIMROCommName_Object=MibTableColumn
ctOrpHSIMROCommName=_CtOrpHSIMROCommName_Object((1,3,6,1,4,1,52,4,1,1,15,1,1,7),_CtOrpHSIMROCommName_Type())
ctOrpHSIMROCommName.setMaxAccess(_B)
if mibBuilder.loadTexts:ctOrpHSIMROCommName.setStatus(_A)
_CtOrpHSIMRWCommName_Type=OctetString
_CtOrpHSIMRWCommName_Object=MibTableColumn
ctOrpHSIMRWCommName=_CtOrpHSIMRWCommName_Object((1,3,6,1,4,1,52,4,1,1,15,1,1,8),_CtOrpHSIMRWCommName_Type())
ctOrpHSIMRWCommName.setMaxAccess(_B)
if mibBuilder.loadTexts:ctOrpHSIMRWCommName.setStatus(_A)
_CtOrpHSIMSUCommName_Type=OctetString
_CtOrpHSIMSUCommName_Object=MibTableColumn
ctOrpHSIMSUCommName=_CtOrpHSIMSUCommName_Object((1,3,6,1,4,1,52,4,1,1,15,1,1,9),_CtOrpHSIMSUCommName_Type())
ctOrpHSIMSUCommName.setMaxAccess(_B)
if mibBuilder.loadTexts:ctOrpHSIMSUCommName.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'MacAddress':MacAddress,'ctOrpHSIMTable':ctOrpHSIMTable,'ctOrpHSIMEntry':ctOrpHSIMEntry,_E:ctOrpHSIMSlot,_F:ctOrpHSIMIndex,'ctOrpHSIMIfRef':ctOrpHSIMIfRef,'ctOrpHSIMMACAddress':ctOrpHSIMMACAddress,'ctOrpHSIMIPAddress':ctOrpHSIMIPAddress,'ctOrpHSIMSubnetMask':ctOrpHSIMSubnetMask,'ctOrpHSIMROCommName':ctOrpHSIMROCommName,'ctOrpHSIMRWCommName':ctOrpHSIMRWCommName,'ctOrpHSIMSUCommName':ctOrpHSIMSUCommName})